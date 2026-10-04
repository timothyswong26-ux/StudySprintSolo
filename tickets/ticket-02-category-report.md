# Finish the category breakdown report

**Difficulty:** S

## Description

`features/reports.py` has a `category_report(data)` function that is only a stub -
it always returns an empty dict. Finish it so it counts how many cards are in
each category. This is the report the menu's "Category breakdown" option should
eventually use.

## Acceptance criteria

- [ ] `category_report(data)` returns a dict of `{category: number_of_cards}`.
- [ ] Every card in the deck is counted exactly once.
- [ ] An empty deck returns an empty dict (no crash).
- [ ] A test in `tests/` checks the counts against a small sample deck.

## Notes

Touches `features/reports.py` and a test file. The `count_by_category` function
in `core.py` is a good reference for the tally pattern.
