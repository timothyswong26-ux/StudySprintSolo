# Auto-generate a multiple-choice question

**Difficulty:** M

## Description

Some players do better with multiple choice. Given one card, build a
multiple-choice question by mixing its correct answer with a few wrong answers
pulled from other cards.

## Acceptance criteria

- [ ] A new function takes a card plus the full deck and returns the correct
      answer plus 3 distinct wrong options.
- [ ] The 4 options are shuffled so the answer isn't always first.
- [ ] It still works when the deck has fewer than 4 cards (use what's available).
- [ ] A test checks that the correct answer is always among the options.

## Notes

`random.sample` and `random.shuffle` help here. Touches `features/core.py` and a test.
