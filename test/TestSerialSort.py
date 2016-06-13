import os
import sys
import unittest

path = os.path.abspath(os.path.dirname(__file__)) + "/.."
sys.path.append(path)

from pyalgo import serial_sort

class TestSerialSort(unittest.TestCase):
    array = [1, 0, 2, 4, 5, 10, 8, 6, 3, 7, 9]
    result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_heap_sort(self):
        self.assertTrue(self.result == serial_sort.heap_sort(self.array))

    def test_merge_sort(self):
        self.assertTrue(self.result == serial_sort.merge_sort(self.array))

    def test_quick_sort(self):
        self.assertTrue(self.result == serial_sort.quick_sort(self.array))

    def test_insertion_sort(self):
        self.assertTrue(self.result == serial_sort.insertion_sort(self.array))

if __name__ == "__main__":
    unittest.main()

