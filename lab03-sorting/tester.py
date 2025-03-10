## Lab03- TESTER ##

# This file will test the sorting algorithms in sorting.py
# Call using python -m unittest tester.py #

import sorting
import random
import time
import unittest

from sorting import bubblesort, selectionsort, insertionsort

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.data = [random.randint(0, 100) for _ in range(10)]
        self.sorted_data = sorted(self.data)

    def test_bubblesort(self):
        self.assertEqual(bubblesort(self.data.copy()), self.sorted_data)

    def test_selectionsort(self):
        self.assertEqual(selectionsort(self.data.copy()), self.sorted_data)

    def test_insertionsort(self):
        self.assertEqual(insertionsort(self.data.copy()), self.sorted_data)

    def test_bubblesort_all_same(self):
        data = [5] * 10
        self.assertEqual(bubblesort(data.copy()), data)

    def test_selectionsort_all_same(self):
        data = [5] * 10
        self.assertEqual(selectionsort(data.copy()), data)

    def test_insertionsort_all_same(self):
        data = [5] * 10
        self.assertEqual(insertionsort(data.copy()), data)

    def test_bubblesort_sorted(self):
        data = list(range(10))
        self.assertEqual(bubblesort(data.copy()), data)

    def test_selectionsort_sorted(self):
        data = list(range(10))
        self.assertEqual(selectionsort(data.copy()), data)

    def test_insertionsort_sorted(self):
        data = list(range(10))
        self.assertEqual(insertionsort(data.copy()), data)

    def test_bubblesort_reverse(self):
        data = list(range(10, 0, -1))
        self.assertEqual(bubblesort(data.copy()), list(range(1, 11)))

    def test_selectionsort_reverse(self):
        data = list(range(10, 0, -1))
        self.assertEqual(selectionsort(data.copy()), list(range(1, 11)))

    def test_insertionsort_reverse(self):
        data = list(range(10, 0, -1))
        self.assertEqual(insertionsort(data.copy()), list(range(1, 11)))

if __name__ == '__main__':
    unittest.main()