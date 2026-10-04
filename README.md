# StudySprint

A small flashcard and quiz trainer you run in the terminal. Load a deck of
cards from a JSON file, quiz yourself, and see your score at the end.

This is your squad's starting product for **Elite 101**. It already runs. Your
job over the term is to grow it one ticket at a time, the way a real software
team does.

## Run it

```bash
python main.py
```

## Run the tests

```bash
python -m unittest
```

Both commands work from the root of this repo with no setup and no installs.

## Where the work comes from

Every change you make starts from a ticket. There are two places to read them,
and they say the same thing:

- **`tickets/`** - the eight tickets as files in this repo. Start here if you
  just cloned it.
- **The Issues tab** - the same eight tickets, on GitHub, where your squad
  claims them and links them to pull requests.

Each ticket names a difficulty (S or M), what "done" looks like as a checklist,
and a Notes line telling you which files it touches.

## What is in here

| Path | What it does |
|---|---|
| `main.py` | The menu loop you interact with |
| `storage.py` | Loads and saves the JSON data file |
| `features/core.py` | The deck, the quiz loop, and small helpers |
| `features/reports.py` | Summary reports (half-built on purpose - you finish it via a ticket) |
| `data/studysprint.json` | The card deck and score history |
| `tests/test_core.py` | Example tests to copy from |
| `tickets/` | The eight tickets your squad works through |
| `docs/README.md` | The product guide, plus the Team list you add yourself to |
| `CONTRIBUTING.md` | The Definition of Done and the branch naming rules |

## Before you open your first pull request

Read **[CONTRIBUTING.md](CONTRIBUTING.md)**. A pull request is done only when
all five are true: the ticket is linked, it runs, a squadmate reviewed it, a
test covers it, and the docs reflect the change. Never commit straight to
`main` - it is what a new teammate clones and what the demo runs from.

## Next steps

1. Read **[docs/README.md](docs/README.md)** and add yourself to the Team list.
2. Pick a ticket from `tickets/` or the Issues tab.
3. Branch, build, test, open the pull request.
