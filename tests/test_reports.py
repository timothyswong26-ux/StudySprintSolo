"""Reference tests for the average_score feature (Lesson 12 answer key)."""

import unittest

from features import reports


class TestAverageScore(unittest.TestCase):
    def test_empty_history_is_zero(self):
        self.assertEqual(reports.average_score({"history": []}), 0.0)

    def test_single_score(self):
        self.assertEqual(reports.average_score({"history": [7]}), 7.0)

    def test_several_scores_are_averaged(self):
        self.assertEqual(reports.average_score({"history": [5, 6, 4]}), 5.0)


if __name__ == "__main__":
    unittest.main()
