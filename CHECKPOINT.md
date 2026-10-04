# Checkpoint - after Lesson 12 (Unit Testing)

Reference "on-track" state. A student who fell behind can switch here to rejoin
from a known-good baseline; instructors use it as the worked answer key.

What should be true now:

- The `average_score` feature added in `lesson/12-start` now has tests:
  `tests/test_reports.py` covers the empty-history, single-score, and
  several-scores cases.
- "Test shown" is now part of your Definition of Done.

`python -m unittest` runs both the original and the new tests, all passing.
