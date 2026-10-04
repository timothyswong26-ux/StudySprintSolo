# Import a deck from a CSV file

**Difficulty:** M

## Description

Teachers have decks in spreadsheets. Let a player load extra cards from a CSV
file with columns `question,answer,category` and add them to the current deck.

## Acceptance criteria

- [ ] A new function reads a CSV path and returns a list of card dicts.
- [ ] Each imported card gets a fresh unique `id` (keep going after the last one).
- [ ] A bad path is reported to the player, not a raw crash.
- [ ] A new menu option in `main.py` runs the import.
- [ ] A test covers parsing a small CSV string.

## Notes

The standard-library `csv` module handles the parsing. Touches `features/core.py`
and `main.py`.
