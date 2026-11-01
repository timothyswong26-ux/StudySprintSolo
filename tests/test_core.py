"""Example tests for StudySprint. Two small tests to copy from in Lesson 12."""

import unittest

from features import core


class TestCore(unittest.TestCase):
    def test_check_answer_is_case_insensitive(self):
        card = {"id": 1, "question": "Capital of France?", "answer": "Paris", "category": "geo"}
        self.assertTrue(core.check_answer(card, "paris"))
        self.assertFalse(core.check_answer(card, "London"))

    def test_add_card_gives_a_new_id(self):
        data = {"cards": [{"id": 1, "question": "q", "answer": "a", "category": "general"}]}
        card = core.add_card(data, "New question?", "yes")
        self.assertEqual(card["id"], 2)
        self.assertEqual(len(data["cards"]), 2)
    def category_report(data):
        report = {}
        cards = []
        if isinstance(data, dict):
            cards = data.get("cards", [])
        elif isinstance(data, list):
            cards = data

        if not cards:
            return report

        for card in cards:
            if isinstance(card, dict):
                category = card.get("category", "Uncategorized")
            else:
                category = getattr(card, "category", "Uncategorized")
                
            report[category] = report.get(category, 0) + 1
        return report


if __name__ == "__main__":
    unittest.main()
