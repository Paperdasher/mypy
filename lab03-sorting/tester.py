## Lab03- TESTER ##

# This file will test the sorting algorithms in sorting.py

import sorting
import random
import time
import unittest

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.data = [random.randint(0, 100) for _ in range(10)]
        self.sorted_data = sorted(self.data)

    def test_bubblesort(self):
        self.assertEqual(sorting.bubblesort(self.data.copy()), self.sorted_data)

    def test_selectionsort(self):
        self.assertEqual(sorting.selectionsort(self.data.copy()), self.sorted_data)

    def test_insertionsort(self):
        self.assertEqual(sorting.insertionsort(self.data.copy()), self.sorted_data)

if __name__ == '__main__':
    unittest.main()