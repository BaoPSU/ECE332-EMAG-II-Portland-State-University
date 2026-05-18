# Lab 2 — Wireless Power Transfer — TA Feedback

**Grade:** 98 / 100
**TA:** Jeff Dinsmore
**Date:** May 17, 2026 at 8:38 PM
**Attempt:** 1

## Comments

1. **Coil tuning mismatch.** The transmitter coil was tuned to 6.78 MHz but the receiver coil was tuned to 13.56 MHz. They were supposed to be the same frequency. This is likely why the antennas had to be so close together to light the bulb.

2. **Question 3 — lower frequency / bigger loop reasoning.** The lower frequency from the bigger loop would actually cause a *drop* in induced voltage, not a gain. Going to a bigger loop may not increase efficiency and could actually reduce it.

   The relevant equation is the induced EMF from mutual inductance:
   $$\varepsilon = -M \frac{di}{dt}$$

   A lower $di/dt$ (from lower frequency) directly reduces $\varepsilon$, regardless of how big the loop is.

## Takeaways for future labs

- Match transmitter and receiver resonance frequencies before testing range/efficiency.
- When discussing antenna efficiency in writeups, anchor the reasoning to the actual physics equation. Bigger loop $\ne$ automatically more efficient — frequency and $di/dt$ matter directly.
