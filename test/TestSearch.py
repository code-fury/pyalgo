import os
import sys
import unittest
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("debug logger")

path = os.path.abspath(os.path.dirname(__file__)) + "/.."
sys.path.append(path)

from pyalgo import search


class TextSearch(unittest.TestCase):
    text = "ABBAACBCB"
    pattern = "ACBCB"
    false_pattern = "ASDQ"

    def test_kmp_search(self):
        self.assertTrue(search.kmp_search(self.text, self.pattern) == 4)
        self.assertTrue(search.kmp_search(self.text, self.false_pattern) == -1)

    def test_rabin_karp_search(self):
            self.assertTrue(search.rabin_karp_search(self.text, self.pattern) == 4)
            self.assertTrue(search.rabin_karp_search(self.text, self.false_pattern) == -1)

    def test_boyer_moore_search(self):
        self.assertTrue(search.boyer_moore_search(self.text, self.pattern) == 4)
        self.assertTrue(search.boyer_moore_search(self.text, self.false_pattern) == -1)

if __name__ == "__main__":
    unittest.main()

