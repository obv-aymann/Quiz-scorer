"""
Test File for Quiz Scorer
Created by: Ayman
"""

import unittest
from quiz_scorer import (
    calculate_total,
    calculate_average,
    get_highest,
    get_lowest,
    add_score
)

class TestQuizScorer(unittest.TestCase):

    def test_calculate_total(self):
        self.assertEqual(calculate_total([10, 20, 30]), 60)

    def test_calculate_average(self):
        self.assertEqual(calculate_average([10, 20, 30]), 20)

    def test_get_highest(self):
        self.assertEqual(get_highest([10, 50, 30]), 50)

    def test_get_lowest(self):
        self.assertEqual(get_lowest([10, 50, 30]), 10)

    def test_add_score(self):
        self.assertEqual(add_score([10, 20], 30), [10, 20, 30])


if __name__ == "__main__":
    unittest.main()