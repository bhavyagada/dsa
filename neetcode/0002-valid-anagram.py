import unittest
from collections import defaultdict

class Solution:
    """
    Given two strings s and t, return true if t is an "anagram" of s, and false otherwise.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_counts, t_counts = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            s_counts[s[i]] += 1
            t_counts[t[i]] += 1

        return s_counts == t_counts

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))

    def test_example_2(self):
        self.assertFalse(self.solution.isAnagram("rat", "car"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isAnagram("", ""))

    def test_single_character(self):
        self.assertTrue(self.solution.isAnagram("a", "a"))

    def test_different_lengths(self):
        self.assertFalse(self.solution.isAnagram("hello", "world!"))

    def test_same_characters_different_counts(self):
        self.assertFalse(self.solution.isAnagram("aab", "abb"))

    def test_unicode_characters(self):
        self.assertTrue(self.solution.isAnagram("こんにちは", "はちにんこ"))

    def test_all_same_character(self):
        self.assertTrue(self.solution.isAnagram("aaaaa", "aaaaa"))

    def test_case_sensitive(self):
        self.assertFalse(self.solution.isAnagram("Anagram", "nagaram"))

    def test_long_strings(self):
        s = "a" * 50000 + "b" * 50000
        t = "b" * 50000 + "a" * 50000
        self.assertTrue(self.solution.isAnagram(s, t))

    def test_special_characters(self):
        self.assertTrue(self.solution.isAnagram("!@#$%^&*()", "()&*^%$#@!"))

    def test_mixed_characters(self):
        self.assertTrue(self.solution.isAnagram("a1b2c3", "3c2b1a"))

if __name__ == '__main__':
    unittest.main()
