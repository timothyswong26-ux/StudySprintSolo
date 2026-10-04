# Track the player's best answer streak

**Difficulty:** M

## Description

Players love streaks. Add a helper that, given the results of a quiz (a list of
booleans), returns the length of the longest run of correct answers in a row.

## Acceptance criteria

- [ ] A new function `best_streak(results)` lives in `features/core.py`.
- [ ] It returns the length of the longest unbroken run of `True` values.
- [ ] An empty list returns `0`.
- [ ] All-wrong returns `0`; all-correct returns the length of the list.
- [ ] A test in `tests/` covers a mixed streak and the empty case.

## Notes

Touches `features/core.py` and a test file. Think about a running counter and a
"best so far" counter.
