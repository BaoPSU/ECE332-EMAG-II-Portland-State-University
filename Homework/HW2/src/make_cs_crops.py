"""
Generate cs_crops/*.png for HW2_Generate.tex.

Renders the Midterm 1 cheat sheet PDF at 300 DPI and crops named regions
that correspond to the eboxes HW2 problems reference.

Bounding boxes are tuned by inspection of the rendered page at 300 DPI
(2550 x 3300 px). Adjust the (x0, y0, x1, y1) tuples if cropping looks off.
"""

import subprocess
from pathlib import Path
from PIL import Image

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]  # HW2/src -> HW2 -> Homework -> repo root
CHEATSHEET_PDF = REPO_ROOT / "Notes" / "Cheatsheets" / "Midterm1" / "ECE332_Exam1_cheatsheet.pdf"
OUT_DIR = SCRIPT_DIR / "cs_crops"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Render both pages of the cheat sheet at 300 DPI.
TMP_BASE = Path("/tmp/cs_render")
subprocess.run([
    "pdftoppm", "-r", "300", "-png", str(CHEATSHEET_PDF), str(TMP_BASE),
], check=True)

p1 = Image.open(f"{TMP_BASE}-1.png")  # HW1 content (we may use trig table from here)
p2 = Image.open(f"{TMP_BASE}-2.png")  # HW2 content (most crops come from here)

print("Page 1 size:", p1.size)
print("Page 2 size:", p2.size)

# Page is letter-size at 300 DPI = 2550 x 3300 px.
# 3-column layout, 0.25in side margins (75 px each), 0.3in top (90 px), 0.25in bottom (75 px).
# Header bar adds ~30 px.
# columnsep ~= 5pt = 6 px.
#
# Approximate column x ranges (slight padding for the ebox frame):
COL1 = (60, 870)
COL2 = (880, 1675)
COL3 = (1685, 2495)

# Page 2 vertical regions (eyeballed from the layout).
# PIL crop boxes are (left, upper, right, lower) = (x0, y0, x1, y1).
def box(col, y0, y1):
    return (col[0], y0, col[1], y1)

crops_p2 = {
    # Col 1 sections
    "cs_waveparams":      box(COL1, 120, 470),   # PLANE WAVE PARAMETERS (LOSSLESS)
    "cs_losslessEH":      box(COL1, 470, 950),   # LOSSLESS PLANE WAVE E AND H
    "cs_losslessVsLossy": box(COL1, 950, 1620),  # LOSSLESS vs LOSSY comparison
    "cs_direction":       box(COL1, 1620, 1860), # DIRECTION OF PROPAGATION
    "cs_kxE":             box(COL1, 1860, 2380), # k x E DIRECTION TABLE
    "cs_trig":            box(COL1, 2380, 2680), # TRIG PHASE SHIFTS

    # Col 2 sections
    "cs_polarization":    box(COL2, 120, 800),   # POLARIZATION GENERAL WAVE (with ellipse fig)
    "cs_chi":             box(COL2, 800, 1080),  # chi SHAPE & HANDEDNESS
    "cs_quadrant":        box(COL2, 1080, 1450), # QUADRANT RULE FOR tan(2 gamma)
    "cs_phasor":          box(COL2, 1450, 1880), # PHASOR <-> TIME DOMAIN
    "cs_circular":        box(COL2, 1880, 2230), # CIRCULAR POLARIZATION TIME DOMAIN
    "cs_retarded":        box(COL2, 2230, 2680), # RETARDED POTENTIALS

    # Col 3 sections
    "cs_lossyclass":      box(COL3, 120, 380),   # LOSSY MEDIA CLASSIFICATION
    "cs_lossyexact":      box(COL3, 380, 780),   # ANY MEDIUM EXACT
    "cs_skindepth":       box(COL3, 780, 960),   # SKIN DEPTH
    "cs_lowloss":         box(COL3, 960, 1180),  # LOW-LOSS MEDIUM
    "cs_goodconductor":   box(COL3, 1180, 1410), # GOOD CONDUCTOR
    "cs_surfaceres":      box(COL3, 1410, 1820), # SURFACE RESISTANCE
    "cs_poynting":        box(COL3, 1820, 2310), # AVERAGE POWER DENSITY (POYNTING)
    "cs_decibels":        box(COL3, 2310, 2500), # DECIBELS & ATTENUATION
}

for name, box in crops_p2.items():
    crop = p2.crop(box)
    out = OUT_DIR / f"{name}.png"
    crop.save(out, "PNG", optimize=True)
    print(f"  wrote {out.name} ({crop.size[0]}x{crop.size[1]})")

print("done")
