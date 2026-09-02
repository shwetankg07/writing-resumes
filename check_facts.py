#!/usr/bin/env python3
"""Fail a resume draft that claims things the profile does not contain.

    python3 check_facts.py resume.tex profile.yml

Flags every number in the draft that is absent from profile.yml, plus any
[ASK:] marker left in. Exit 1 if anything is flagged.

Known ceiling: this proves a number EXISTS in the profile, not that it is used
in the right place - "40 min" in the profile will clear "40%" in the draft. It
catches invented magnitudes, which is the common failure; it does not catch a
real number moved to the wrong claim.

# ponytail: numeric claims + markers only. Prose claims ("led the team") need a
# human read; add a claim extractor if fabricated prose shows up in practice.
"""
import re
import sys

URL = re.compile(r"https?://\S+|\b[\w.-]+\.(?:com|dev|io|org|net|sh|site)\b\S*")
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")
LATEX_LENGTHS = re.compile(
    r"\\(?:vspace|hspace|setlength|rule|hrule|fontsize|linespread|arraystretch|"
    r"columnsep|baselineskip)\*?(?:\[[^\]]*\])?(?:\{[^{}]*\})*"
)


def strip_latex(text):
    body = re.split(r"\\begin\{document\}", text, maxsplit=1)
    text = body[1] if len(body) > 1 else text
    text = LATEX_LENGTHS.sub(" ", text)
    text = re.sub(r"^\s*%.*$", " ", text, flags=re.M)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", " ", text)
    return text.replace("{", " ").replace("}", " ")


def strip_html(text):
    text = re.sub(r"<(style|script)\b.*?</\1>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return text.replace("&bull;", " ").replace("&amp;", "&")


def visible_text(path):
    raw = open(path, encoding="utf-8").read()
    if path.endswith((".tex", ".latex")):
        return strip_latex(raw)
    if path.endswith((".html", ".htm")):
        return strip_html(raw)
    return raw


def norm(tok):
    t = tok.replace(",", "")
    try:
        f = float(t)
    except ValueError:
        return t
    return str(int(f)) if f == int(f) else str(f)


def numbers(text):
    return {norm(m) for m in NUM.findall(URL.sub(" ", text))}


def check(draft_path, profile_path):
    text = visible_text(draft_path)
    known = numbers(open(profile_path, encoding="utf-8").read())
    problems = []

    for n, line in enumerate(text.splitlines(), 1):
        for tok in NUM.findall(URL.sub(" ", line)):
            if norm(tok) not in known:
                problems.append((n, f"unverified number {tok!r}", line.strip()))
        if "[ASK:" in line:
            problems.append((n, "unanswered [ASK:] marker", line.strip()))
    return problems


def self_test():
    import tempfile, os

    d = tempfile.mkdtemp()
    prof = os.path.join(d, "p.yml")
    open(prof, "w").write("facts:\n  - cut batch from 40 min to 9 min\n  - 9,298 trains\n")

    tex = os.path.join(d, "r.tex")
    open(tex, "w").write(
        "\\usepackage[margin=0.6in]{geometry}\n\\begin{document}\n"
        "\\vspace{7pt}\n\\item Cut the batch from 40 min to 9 min.\n"
        "\\item Parsed 9,298 trains.\n\\end{document}\n"
    )
    assert check(tex, prof) == [], check(tex, prof)  # preamble + \vspace ignored

    bad = os.path.join(d, "b.tex")
    open(bad, "w").write("\\begin{document}\n\\item Improved performance by 62\\%.\n")
    got = check(bad, prof)
    assert len(got) == 1 and "62" in got[0][1], got

    # the documented ceiling: a real number in the wrong claim still passes
    reused = os.path.join(d, "c.tex")
    open(reused, "w").write("\\begin{document}\n\\item Grew signups 40\\%.\n")
    assert check(reused, prof) == []

    html = os.path.join(d, "r.html")
    open(html, "w").write(
        "<style>body{font:10.5pt/1.4 sans-serif;margin:14mm}</style>\n"
        "<li>Parsed 9298 trains.</li>\n<li>[ASK: how many users?]</li>\n"
    )
    got = check(html, prof)
    assert len(got) == 1 and "ASK" in got[0][1], got  # css ignored, marker caught
    print("self-test ok")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
        sys.exit(0)
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    found = check(sys.argv[1], sys.argv[2])
    for line_no, why, text in found:
        print(f"{sys.argv[1]}:{line_no}: {why}\n    {text}")
    if found:
        print(f"\n{len(found)} unverified claim(s). Get the fact, or cut the line.")
        sys.exit(1)
    print("every number in the draft traces to the profile.")
