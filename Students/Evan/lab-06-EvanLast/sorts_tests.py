import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_selection_best_case(self):
        pass

    def test_selection_avg_case(self):
        pass

    def test_selection_worst_case(self):
        pass

    def test_insertion_best_case(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        insertion = insertion_sort(nums)
        self.assertEqual(insertion, 8)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_insertion_avg_case(self):
        pass

    def test_insertion_worst_case(self):
        pass


if __name__ == '__main__': 
    unittest.main()
