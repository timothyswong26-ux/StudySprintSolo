# Show a deck progress bar

**Difficulty:** S

## Description

While taking the quiz, show the player how far along they are, like
`[###-------] 3/8`, so a long deck feels less endless.

## Acceptance criteria

- [ ] A new function turns a "current / total" pair into a text bar string.
- [ ] The bar length is fixed (e.g. 10 characters) regardless of deck size.
- [ ] `0/total` and `total/total` both render without error.
- [ ] The quiz prints the bar before each question.
- [ ] A test checks the bar string for a couple of positions.

## Notes

Pure string building - no new packages. Touches `features/core.py` and `main.py`.
