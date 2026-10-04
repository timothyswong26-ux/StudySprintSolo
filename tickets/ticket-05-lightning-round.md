# Add a timed lightning round

**Difficulty:** M

## Description

Add a fast quiz mode that shows how long the player took to get through the deck,
so they can try to beat their own time.

## Acceptance criteria

- [ ] A new menu option runs a "lightning round" quiz.
- [ ] It reports the total seconds taken alongside the score.
- [ ] The timing uses the standard library (no new packages).
- [ ] The normal quiz still works unchanged.
- [ ] A short note in the README documents the new mode.

## Notes

`time.time()` before and after the loop is enough. Touches `main.py` and maybe
a small helper in `features/core.py`.
