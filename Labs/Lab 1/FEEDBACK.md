# Lab 1 — Signal Integrity — TA Feedback

**Grade:** 95 / 100
**TA:** Jeff Dinsmore
**Submitted:** April 9, 2026 at 12:29 PM
**Feedback dates:** April 27, 2026 at 5:05 PM and April 28, 2026 at 10:58 PM

## Comments

1. **Missing 3 GHz plots.** The plots shown in the report are at 1 GHz, but the required frequency was 3 GHz. Run the simulation again at 3 GHz for the proper write-up.

2. **Coupling mechanism — wrong field.** Magnetic field is the dominant field affecting coupling in traces that are parallel or at a close angle. Electric field can dominate in *high-impedance* lines, but the lines in this lab are *low impedance*, so it's magnetic coupling. Don't default to E-field.

3. **"How can coupling be reduced?" — wrong answer.** The report says "keep traces as short as possible". The correct answer is **differential signaling**. Shortening traces reduces coupling length but doesn't address the mechanism. Differential signaling cancels common-mode pickup directly.

## Takeaways for future labs

- Check the frequency spec carefully and re-run simulations at the exact required frequency before plotting.
- For coupling questions, classify the line first (low-Z $\to$ magnetic dominant, high-Z $\to$ electric dominant) before reasoning about which field couples.
- For "how to reduce coupling" questions, lead with **differential signaling** as the primary answer. Trace shortening is secondary.
