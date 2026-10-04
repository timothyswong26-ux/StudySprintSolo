# Add a "review missed cards" mode

**Difficulty:** S

## Description

Right now the quiz runs through every card once and shows a score. Players want
to focus on the cards they got wrong. Add a helper that, given the cards and a
list of results, returns just the cards the player missed so a review round can
use them.

## Acceptance criteria

- [ ] A new function `review_missed(cards, results)` lives in `features/core.py`.
- [ ] `results` is a list of booleans lined up with `cards` (True = correct).
- [ ] It returns the list of cards where the matching result is False.
- [ ] If nothing was missed, it returns an empty list (no crash).
- [ ] A test in `tests/` covers a mixed case and the "nothing missed" case.

## Notes

Touches `features/core.py` and a test file. No changes to the data file needed.
