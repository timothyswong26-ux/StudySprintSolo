"""Reporting helpers for StudySprint.

Heads up: this module is half-built on purpose. `deck_summary` works, but
`category_report` is still a stub with a clear seam to finish (see the tickets).
"""


def deck_summary(data):
    return data["deck_name"] + ": " + str(len(data["cards"])) + " cards"

#ticket two
def category_report(data):
    # TODO(ticket): tally each card into a {category: count} dict and return it.
    # For now this returns an empty report so the menu never crashes.
    report = {}
    return report
    if not data:
        return report
    for card in data:
        if isinstance(card, dict):
            category = card.get("category", "Uncategorized")
        else:
            category = getattr(card, "category", "Uncategorized")
            
        report[category] = report.get(category, 0) + 1
    return report
