# ECE332 — Claude Project Guide

Portland State University, ECE332 Electromagnetics II, Spring 2026.
Owner: Bao Nguyen (baon@pdx.edu). Lab partner: Nick Stites.
Instructor: Mark Martin (marmart2@pdx.edu), FAB 20-10. Office hours T/Th 12:30–1:20.

**Repo:** `BaoPSU/ECE332-EMAG-II-Portland-State-University`
**Syllabus:** `syllabus.pdf` at repo root — check it first for grading/coverage questions.

## Exams (from syllabus, Method of Evaluation)
- **Midterm 1** — May 7, 2026. Covers lectures 1–10 + HW1, HW2. Worth 25%.
- **Final exam** — date TBD. Covers lecture 11 onward (second half). **NOT cumulative.** Worth 25%.
- See `Notes/Cheatsheets/Midterm1/COVERAGE.md` and `Notes/Cheatsheets/Final/COVERAGE.md` for full topic lists.

## Grade weights
Labs 20% · HW 30% · Midterm 25% · Final 25%. Curve possible at end of term.

---

## Folder Structure

```
Exams/         — exam materials and prep
Homework/      — HW1, HW2, ...
Labs/          — Lab 1, Lab 2, Lab 3, ...
  └── Lab N/   — each lab has .docx, .pdf, and LaTeX versions
                  (files ending in _latex.tex / _latex.pdf are the LaTeX-typeset reports)
Notes/         — lecture PDFs (lecture01..lecture11) and cheat sheets
  └── Cheatsheets/  — see Notes/CLAUDE.md for the cheat sheet workflow
```

---

## Writing Persona (use for lab reports, HW answers, anything graded)

Voice originally captured for ECE 410/510 but it applies across all ECE coursework.
Professional register: keep the structure and connectors, drop casual fillers (no "dude/man/tbh").

### Lead style
- **Lead with the result or key number, not a setup sentence.** Don't open with "In this experiment we will..." or "In free space, a wave...".
- Open with the answer itself, then explain why.
- Anchor every claim to a number from the data, not "the error is significant" but "the error is about 2%".

### Connectors (use these instead of starting new sentences)
- **"About the [topic]"** — primary opener for a new sub-topic. Often standalone with just "About", no "so" prefix.
- **"So about the [topic]"** — same idea but use sparingly (once per page max). Don't stack multiple "so about" openers in a row.
- **"Like, [something]"** — mid-sentence example or analogy ("Like, two plane waves bouncing off the walls").
- **"For example"** — to follow a rule with a concrete number from the lab.
- **"And then"** — for sequence (calculation steps, signal flow).
- **"which"** — to continue a description mid-sentence rather than breaking.
- **"and"** — to connect related thoughts without a sentence break.
- **"so basically"** — landing the conclusion at the end of a paragraph.
- Avoid bare **"so"** as a sentence opener (use it inside "so basically").

### Equation handling
- After every equation, one sentence of plain-language intuition.
- Use "for example" right after a formula to plug in actual measured numbers.

### Approximation language
- "Roughly", "pretty close", "close enough", "about" — when a value is not exact.
- "Exactly" — only when it really is.
- Never drop an uncertain number without flagging it.

### Avoid
- **No em dashes** — rewrite the sentence using "which", "and", "so basically", or split into two sentences.
- No "It is important to note", "It can be seen that", "It was found that" (passive voice).
- No "In my opinion", "I think", "honestly" as openers — they undermine the claim.
- No textbook phrasing like "Let us consider..." or "We shall now derive...".
- No dramatic conclusion sentences. End plain.

### Register
- **Casual (peers, slack, voice notes):** "tbh", "man", "dude" OK.
- **Professional (lab reports, HW, presentations):** same connectors and structure, just drop the casual fillers.
- Either way, never sounds like a textbook.

---

## GitHub Workflow

GitHub token at `/home/bao/.github_token` (already used for ECE424 and other private repos).
Read with `cat /home/bao/.github_token`.

### Push files via API (file paths with spaces — URL-encode)

```python
import base64, json, subprocess, urllib.parse
token = open('/home/bao/.github_token').read().strip()
repo = 'BaoPSU/ECE332-EMAG-II-Portland-State-University'
path = 'Labs/Lab 3/ECE332_Lab3_Waveguides_Official_latex.pdf'
enc = urllib.parse.quote(path)
local = '/home/bao/Documents/GitHub/ECE332-EMAG-II-Portland-State-University/' + path

# Get current SHA
r = subprocess.run(['curl', '-s', '-H', f'Authorization: token {token}',
                    f'https://api.github.com/repos/{repo}/contents/{enc}'],
                   capture_output=True, text=True)
sha = json.loads(r.stdout).get('sha')  # None if creating a new file

with open(local, 'rb') as f:
    content_b64 = base64.b64encode(f.read()).decode()

payload = {'message': 'commit message', 'content': content_b64}
if sha: payload['sha'] = sha

with open('/tmp/payload.json', 'w') as f: json.dump(payload, f)
subprocess.run(['curl', '-s', '-X', 'PUT',
                '-H', f'Authorization: token {token}',
                '-H', 'Content-Type: application/json',
                '-d', '@/tmp/payload.json',
                f'https://api.github.com/repos/{repo}/contents/{enc}'])
```

---

## Homework Files — Naming Convention

Each `Homework/HWN/` folder uses this exact naming, no spaces, no inconsistent case:

| File | Meaning |
|---|---|
| `HWN_Original.pdf` | Instructor's original prompt (what gets handed out in class) |
| `HWN_Blank.pdf` | Bao's Xournal worksheet version with extra space for handwriting |
| `HWN_Submission.pdf` | Bao's completed work that was turned in |
| `hwN_solutions.pdf` | Instructor's official solutions (lowercase) |
| `HWN_Generate.pdf` | Walk-through doc showing which cheat sheet snippets solve each problem |
| `src/` | Folder with LaTeX source, Python scripts, image crops for `HWN_Generate` |

So `HW2/` looks like:
```
Homework/HW2/
├── HW2_Original.pdf
├── HW2_Blank.pdf
├── HW2_Submission.pdf
├── hw2_solutions.pdf
├── HW2_Generate.pdf
└── src/
    ├── HW2_Generate.tex
    ├── make_cs_crops.py
    ├── HW2_P3a.py / .png  (per-problem plots, if any)
    └── cs_crops/
        └── cs_*.png  (cropped eboxes from the midterm cheat sheet)
```

Top-level PDFs are the readable outputs. `src/` holds everything needed to rebuild them. Compile `HW2_Generate.tex` from inside `src/` (the `\graphicspath` resolves to `cs_crops/` relative to that directory), then copy the resulting PDF up to `HW2/`.

`make_cs_crops.py` parses the midterm cheat sheet source `.tex`, pulls out each `\shead{}{}{TITLE}` + `\begin{ebox}...\end{ebox}` block, compiles each one as its own standalone mini-document with the same preamble (colors, `\eq`, `\shead`, `ebox`), then renders to PNG and auto-trims whitespace. To add a new section, add an entry to the `WANT` dict mapping a unique keyword from the section title to the desired output slug, then rerun the script.

`make_p3_plots.py` generates the polarization locus plots, including direction-of-motion arrows (curved for rotating cases, double-headed for linear oscillations).

---

## Lab Reports — LaTeX Convention

- Source: `Labs/Lab N/ECE332_LabN_<topic>_Official_latex.tex`
- PDF: `Labs/Lab N/ECE332_LabN_<topic>_Official_latex.pdf`
- Title page mimics the original PSU handout (Portland State University → Department of Electrical and Computer Engineering → ECE332 → Lab N: Topic → Prepared by: Bao Nguyen, Nick Stites → Term: Spring 2026).
- Always include `\tableofcontents` after the title page.
- Pre-lab multiple choice: show ALL options (a–e), highlight the correct one with `\colorbox{answerhl}{...}` using `\definecolor{answerhl}{RGB}{198,239,206}` (light green).
- Number top-level sections (`\section{}`), keep subsections unnumbered (`\subsection*{}`) so the ToC stays clean.
- Compile twice for ToC: `pdflatex -interaction=nonstopmode <file>.tex` x 2.

---

## TA / Instructor Feedback — `FEEDBACK.md` Convention

Whenever a graded assignment comes back with TA or instructor comments, save them as `FEEDBACK.md` alongside the assignment. Applies to **labs and homework alike**:

- `Labs/Lab N/FEEDBACK.md`
- `Homework/HWN/FEEDBACK.md`

### File template

```markdown
# <Assignment Name> — TA Feedback

**Grade:** XX / 100
**TA:** <Name>
**Submitted:** <date and time>
**Feedback dates:** <date and time>  ← if multiple comments, list them
**Attempt:** <N>  ← if multiple submissions allowed

## Comments

1. **<Short bold lead>.** Plain-English restatement of the TA's point.
   Include the relevant equation in LaTeX math if they cited one:
   $$\varepsilon = -M \frac{di}{dt}$$

2. **<Next point>.** ...

## Takeaways for future labs

- One bullet per actionable lesson, written so future-Bao can apply it without re-reading the comment.
- Anchor each bullet to a rule, equation, or decision criterion (not a vague reminder).
```

### Rules

- **Save the grade exactly as scored**, including the denominator (`98 / 100`, not just `98%`).
- **Don't paraphrase the TA's correction into something nicer.** If the TA says "the answer should have been differential signaling," write that, not "you could have mentioned differential signaling."
- **Add a Takeaways section** at the bottom even if the TA didn't give one. The point is to learn from feedback, not just archive it.
- **Restate equations in LaTeX math** so they render on GitHub.
- **Use the exact date/time stamp** the grading platform shows (e.g., "April 27 at 5:05 PM").
- Multiple feedback comments across different dates: list each date under **Feedback dates** and bundle the comments into the numbered list. Don't make separate sub-sections per date.

### Why bother

Feedback files compound across the term. By final-exam study time, the lab `FEEDBACK.md` files give a quick "what concepts did I actually get wrong on graded work" list — way more useful than re-reading the lab manuals. Same logic for homework: HW feedback files (when they exist) tell you which problem types to drill, even if the cheat sheet has the formula.

### Existing examples

- `Labs/Lab 1/FEEDBACK.md` — Signal integrity, 95/100, Jeff Dinsmore
- `Labs/Lab 2/FEEDBACK.md` — Wireless power, 98/100, Jeff Dinsmore

---

## Cheat Sheets

See `Notes/CLAUDE.md` for the full cheat sheet workflow (3-column layout, color scheme, ebox environment, page-length constraints).

**Important:** Only edit `Notes/Cheatsheets/Midterm1/src/ECE332_Exam1_cheatsheet.tex`.
The standalone `ECE332_HW1_cheatsheet.tex` and `ECE332_HW2_cheatsheet.tex` files are not to be modified.
