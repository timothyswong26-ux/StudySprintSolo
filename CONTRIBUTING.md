# Contributing

Welcome to the team. We work the way a real software team works: every change
rides in on its own branch, opens a pull request, gets one review, and only
then merges. This file is the contract your squad agreed to on Founding Day.

## Definition of Done

A pull request is **done** when all five are true:

- **Ticket linked in PR** - the PR description links the issue it closes.
- **It runs** - `python main.py` still starts and your change works.
- **1 peer review** - a squadmate reviewed and approved it.
- **Test shown** - a test (new or existing) covers the change and passes.
- **Docs touched** - the README or release notes reflect what changed.

If any one of those is missing, the PR is not done yet - it's still in progress.

## Branch naming

One branch per ticket. Name it so anyone can tell what it's for:

```
<yourname>/<short-description>     e.g.  avery/streak-tracking
fix/<short-description>            e.g.  fix/save-crash
```

Never commit straight to `main`. `main` is what a new teammate clones and what
the demo runs from - it always has to work.

## Pull request checklist

Before you request review, put this in the PR description and check it off:

- [ ] Closes #<ticket-number>
- [ ] I ran `python main.py` and the feature works
- [ ] I ran `python -m unittest` and tests pass
- [ ] I updated the README / release notes
- [ ] I requested one squadmate's review

## Reviewing a teammate's PR

You're not looking for perfect - you're checking three things:

1. **Does it run?** Pull the branch, run it.
2. **Does it match the ticket?** Read the acceptance criteria.
3. **Is it readable?** Could you change it next week without asking them?

Leave one specific piece of praise and, if needed, one specific request.
"Approve" only when the Definition of Done is met.
