"""Reporting helpers for StudySprint.

Heads up: this module is half-built on purpose. `deck_summary` works, but
`category_report` is still a stub with a clear seam to finish (see the tickets).
"""


def deck_summary(data):
    return data["deck_name"] + ": " + str(len(data["cards"])) + " cards"


def category_report(data):
    # TODO(ticket): tally each card into a {category: count} dict and return it.
    # For now this returns an empty report so the menu never crashes.
    report = {}
    return report


def average_score(data):
    """Average of the past quiz scores in data['history'].

    Returns a float rounded to one decimal place. An empty history returns 0.0.
    """
    history = data["history"]
    if not history:
        return 0.0
    return round(sum(history) / len(history), 1)
