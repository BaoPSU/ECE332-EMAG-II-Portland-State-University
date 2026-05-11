# ECE332 — Claude Project Guide

Portland State University, ECE332 Electromagnetics II, Spring 2026.
Owner: Bao Nguyen (baon@pdx.edu). Lab partner: Nick Stites.

**Repo:** `BaoPSU/ECE332-EMAG-II-Portland-State-University`

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

## Lab Reports — LaTeX Convention

- Source: `Labs/Lab N/ECE332_LabN_<topic>_Official_latex.tex`
- PDF: `Labs/Lab N/ECE332_LabN_<topic>_Official_latex.pdf`
- Title page mimics the original PSU handout (Portland State University → Department of Electrical and Computer Engineering → ECE332 → Lab N: Topic → Prepared by: Bao Nguyen, Nick Stites → Term: Spring 2026).
- Always include `\tableofcontents` after the title page.
- Pre-lab multiple choice: show ALL options (a–e), highlight the correct one with `\colorbox{answerhl}{...}` using `\definecolor{answerhl}{RGB}{198,239,206}` (light green).
- Number top-level sections (`\section{}`), keep subsections unnumbered (`\subsection*{}`) so the ToC stays clean.
- Compile twice for ToC: `pdflatex -interaction=nonstopmode <file>.tex` x 2.

---

## Cheat Sheets

See `Notes/CLAUDE.md` for the full cheat sheet workflow (3-column layout, color scheme, ebox environment, page-length constraints).

**Important:** Only edit `Notes/Cheatsheets/Midterm1/src/ECE332_Exam1_cheatsheet.tex`.
The standalone `ECE332_HW1_cheatsheet.tex` and `ECE332_HW2_cheatsheet.tex` files are not to be modified.
