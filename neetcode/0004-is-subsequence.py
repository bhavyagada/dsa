import unittest

class Solution:
    """
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]: i += 1
            j += 1

        return len(s) == i

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isSubsequence("abc", "ahbgdc"))

    def test_example_2(self):
        self.assertFalse(self.solution.isSubsequence("axc", "ahbgdc"))

    def test_empty_s(self):
        self.assertTrue(self.solution.isSubsequence("", "ahbgdc"))

    def test_empty_t(self):
        self.assertFalse(self.solution.isSubsequence("abc", ""))

    def test_both_empty(self):
        self.assertTrue(self.solution.isSubsequence("", ""))

    def test_s_longer_than_t(self):
        self.assertFalse(self.solution.isSubsequence("abcde", "abc"))

    def test_same_string(self):
        self.assertTrue(self.solution.isSubsequence("abc", "abc"))

    def test_s_at_beginning_of_t(self):
        self.assertTrue(self.solution.isSubsequence("abc", "abcdefg"))

    def test_s_at_end_of_t(self):
        self.assertTrue(self.solution.isSubsequence("efg", "abcdefg"))

    def test_s_scattered_in_t(self):
        self.assertTrue(self.solution.isSubsequence("adf", "abcdefg"))

    def test_repeated_characters(self):
        self.assertTrue(self.solution.isSubsequence("aaa", "aaaaa"))
        self.assertFalse(self.solution.isSubsequence("aaa", "aa"))

    def test_long_strings(self):
        s = "a" * 100
        t = "b" * 9900 + "a" * 100
        self.assertTrue(self.solution.isSubsequence(s, t))

    def test_almost_subsequence(self):
        self.assertFalse(self.solution.isSubsequence("abc", "acb"))

if __name__ == '__main__':
    unittest.main()
