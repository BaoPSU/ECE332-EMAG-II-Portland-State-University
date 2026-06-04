# What Needs Work — Future Handoff

> **For whoever picks this repo up next** (capstone team, future student, collaborator):
> Bao maintains the git but he's not the lead — he's the organizer / student.
> Everything below is **programming / tooling debt**, not academic content.
> Pick anything off this list, work it, send a PR. Cross out the items as you go.

This file is the handoff. Keep it current.

---

## How this repo is currently structured

- `Homework/HWN/` — handouts, submissions, solutions, walkthrough PDFs (`HWN_Generate.pdf`), Python helpers
- `Labs/Lab N/` — lab manuals, reports (LaTeX-typeset versions of the official PSU `.docx`), feedback files
- `Notes/Cheatsheets/Exam1/` and `Notes/Cheatsheets/Final/` — exam cheat sheets (.tex sources + compiled PDFs)
- `Notes/Textbook/tables/` — cropped textbook tables used as `\includegraphics` in cheat sheets
- `Notes/CLAUDE.md` and root `CLAUDE.md` — the existing manual workflow these items would replace

Built artifacts (`.aux`, `.log`, `.synctex.gz`, intermediate `.pdf`) are mixed into the tree. That's part of the debt.

---

## Build / automation

- [ ] **Makefile for cheat sheets.** One `make` command to compile any cheat sheet from its `src/` folder and copy the PDF up to the parent. Replaces the manual `cd src && pdflatex ... && cp ../` dance.
- [ ] **Auto-regenerate `cs_crops/*.png` when the cheat sheet `.tex` changes.** Right now `make_cs_crops.py` has to be run manually after every edit — easy to forget (see the warning section in `Notes/CLAUDE.md`). Wire into the Makefile or a file-watcher.
- [ ] **One-shot Generate rebuild.** `make hw4-generate` should: compile cheat sheet → regen crops → recompile Generate → copy PDF up. Right now it's 4 manual steps.
- [ ] **CI on push.** GitHub Actions to compile every `.tex` in the repo and fail the build if any errors. Catches "compiles on my machine" drift.
- [ ] **Auto page-count check.** Workflow says cheat sheets "must stay 1 page" but there's no check. Script that compiles + greps `Output written on … (N pages)` and fails CI if N > expected.

## Code reuse / DRY

- [ ] **Shared LaTeX preamble.** Every cheat sheet (`ECE332_Exam1_cheatsheet.tex`, `ECE332_HW1_cheatsheet.tex`, …, `ECE332_Final_cheatsheet.tex`) re-defines the same colors, `\eq`, `\shead`, `ebox` env. Pull into a single `cheatsheet_preamble.sty` and `\usepackage` it.
- [ ] **Consolidate `make_cs_crops.py`.** Duplicated across `Homework/HW*/src/` folders. One canonical version + per-HW config dict.
- [ ] **Consolidate `make_p*_plot.py` scripts.** Every HW has its own plot helper. Common matplotlib config (font sizes, color palette, output DPI) should live in one place.
- [ ] **GitHub push helper.** The `import base64, json, subprocess, urllib.parse` block in `CLAUDE.md` gets copy-pasted into every one-off `/tmp/push_*.py`. Wrap it in `tools/push_files.py` that takes a list of `(path, message)` tuples.
- [ ] **Color palette as a single source.** Colors are redefined identically in 4+ `.tex` files. Pull into the shared preamble.

## Repo hygiene

- [ ] **Proper `.gitignore`.** Currently `.aux` / `.log` / `.synctex.gz` LaTeX cruft slips into commits. Add a real LaTeX `.gitignore`.
- [ ] **Standardize naming.** Some HW PDFs use `Hw4` (capital H, lowercase w), others `HW4`. The `CLAUDE.md` convention says `HWN_*.pdf` (uppercase). Audit and rename.
- [ ] **One `tables/` folder.** `Notes/Textbook/tables/` and `Homework/HW3/tables/` have the same 3 PNGs (Table 8-1, 8-2, 8-3). Symlink or move to one location and reference from both.
- [ ] **Drop legacy build artifacts.** `Notes/Cheatsheets/Final/src/ECE332_HW3_cheatsheet.aux/.log/.pdf` etc. are committed artifacts. Move to build output / gitignore.

## Tooling

- [ ] **Pre-commit hook.** Block commits that include `.aux`, `.log`, `.synctex.gz`, or `__pycache__`. Forces a clean tree.
- [ ] **PDF diff in PRs.** When a cheat sheet `.tex` changes, surface a visual diff of the rendered PDF (CI artifact or `diff-pdf` comment).
- [ ] **Python script linting.** `make_cs_crops.py` and friends have no formatter / lint config. Add `ruff` and a tiny `pyproject.toml`.
- [ ] **Track Python deps.** Currently every plot script implicitly assumes `numpy`, `matplotlib`, `PyMuPDF` are installed. Add `requirements.txt` so a fresh clone is reproducible.

## LaTeX / content tooling

- [ ] **Render textbook tables in LaTeX.** Table 8-2 and 8-3 currently live as PNG screenshots in `Notes/Textbook/tables/`. Rendering them in LaTeX (instead of `\includegraphics`) would make them searchable, resizable, and editable.
- [ ] **Template `HW*_Generate.tex`.** Each HW Generate has a slightly different preamble + structure. Standardize so a new HW is a copy-paste away.
- [ ] **Equation-first lint.** `CLAUDE.md` says Generates should start each sub-part with the goal equation. No automated check — it's eyeballed. A grep-based smoke test would catch most violations.

---

## Quick start for the next person

1. **Read `CLAUDE.md` (root) and `Notes/CLAUDE.md`.** These describe the current manual workflow.
2. **Pick the lowest-hanging item:** "Proper `.gitignore`" or "Standardize naming." Both are 10-minute wins.
3. **Then tackle the Makefile.** That single change removes the most-cited pain point ("did you regenerate the crops?").
4. **Then CI.** Once builds are automated, the rest of the items become easier to validate.

Bao maintains the academic content separately (see `Notes/Cheatsheets/Final/FOCUS.md`). This file is strictly for the developer-experience side of the repo.
