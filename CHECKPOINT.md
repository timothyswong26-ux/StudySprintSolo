# Checkpoint - after Lesson 10 (Debugging I)

Reference "on-track" state. A student who fell behind can switch here to rejoin
from a known-good baseline; instructors use it as the worked answer key.

What should be true now:

- Both seeded logic bugs from `lesson/10-start` are fixed: `run_quiz` returns
  `score` (not `len(cards)`), and `percent_correct` divides by `total`
  (not `total - 1`).
- `features/core.py` now matches `main` - `main` is the correct reference.

`python -m unittest` passes.
