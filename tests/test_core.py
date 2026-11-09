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
from features.core import review_missed
def test_review_missed_mixed():
    cards = ["test1", "test2", "test3"]
    results = [True, False, False]
    assert review_missed(cards, results) == ["test2", "test3"]

def test_review_missed_nothing_missed():
    cards = ["test1", "test2"]
    results = [True, True]
    assert review_missed(cards, results) == []

from features.core import best_streak

def test_best_streak_mixed():
    assert best_streak([True, True, False, True, True, True, False]) == 3

def test_best_streak_empty():
    assert best_streak([]) == 0

def test_best_streak_all_wrong():
    assert best_streak([False, False, False]) == 0

def test_best_streak_all_correct():
    assert best_streak([True, True, True]) == 3


import io
from features.core import import_cards_from_csv

def test_import_cards_from_csv(monkeypatch):
    csv_data = "question,answer\nWhat is 2+2?,4\nCapital of France?,Paris"
    def mock_open(*args, **kwargs):
        return io.StringIO(csv_data)
    
    monkeypatch.setattr("builtins.open", mock_open)
    
    cards = import_cards_from_csv("dummy_path.csv", start_id=10)
    
    assert len(cards) == 2
    assert cards[0] == {"id": 10, "question": "What is 2+2?", "answer": "4"}
    assert cards[1] == {"id": 11, "question": "Capital of France?", "answer": "Paris"}

from features.core import generate_multiple_choice

def test_generate_multiple_choice():
    deck = [
        {"id": 1, "question": "Capital of France?", "answer": "Paris"},
        {"id": 2, "question": "Capital of UK?", "answer": "London"},
        {"id": 3, "question": "Capital of Germany?", "answer": "Berlin"},
        {"id": 4, "question": "Capital of Spain?", "answer": "Madrid"},
        {"id": 5, "question": "Capital of Italy?", "answer": "Rome"}
    ]
    card = deck[0]  # Correct answer is "Paris"
    
    options = generate_multiple_choice(card, deck)

    assert card["answer"] in options
    assert len(options) <= 4
    assert len(options) == len(set(options))  # All options are distinct

from features.core import progress_bar

def test_progress_bar_edge_cases():
    # 0/8 edge case
    assert progress_bar(0, 8) == "[----------] 0/8"
    
    # Full/total edge case
    assert progress_bar(8, 8) == "[##########] 8/8"

def test_progress_bar_mixed():
    # 3/8 position (3/8 * 10 = 3.75, rounded to 4 filled chars)
    assert progress_bar(3, 8) == "[####------] 3/8"

if __name__ == "__main__":
    unittest.main()
