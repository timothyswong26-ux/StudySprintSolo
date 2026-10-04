# Save each quiz score to history

**Difficulty:** S

## Description

The data file already has a `history` list, but scores never get saved to it.
After a quiz finishes, append the score so players can look back at past runs.

## Acceptance criteria

- [ ] After a quiz, the score is appended to `data["history"]`.
- [ ] The change is written to disk with `storage.save_data`.
- [ ] A new menu option prints the last few scores from history.
- [ ] A test checks that recording a score grows the history list.

## Notes

Touches `main.py` and possibly a small helper in `features/core.py`.
