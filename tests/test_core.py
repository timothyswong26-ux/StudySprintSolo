"""Example tests for StudySprint. Two small tests to copy from in Lesson 12."""

import unittest

from features import core
from features import reports


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
    def test_average_score_with_data(self):
        data = {"history": [5, 6, 4]}
        result = reports.average_score(data)
        self.assertEqual(result, 5.0)
    
    def test_average_score_empty_history(self):
        data = {"history": []}
        result = reports.average_score(data)
        self.assertEqual(result, 0.0)


if __name__ == "__main__":
    unittest.main()
