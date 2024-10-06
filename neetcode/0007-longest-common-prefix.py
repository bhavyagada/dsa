import unittest
from typing import List

class Solution:
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]: return prefix
            prefix += strs[0][i]
        return prefix

class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestCommonPrefix(["flower","flow","flight"]), "fl")

    def test_example_2(self):
        self.assertEqual(self.solution.longestCommonPrefix(["dog","racecar","car"]), "")

    def test_single_string(self):
        self.assertEqual(self.solution.longestCommonPrefix(["hello"]), "hello")

    def test_all_same_strings(self):
        self.assertEqual(self.solution.longestCommonPrefix(["aa","aa","aa"]), "aa")

    def test_no_common_prefix(self):
        self.assertEqual(self.solution.longestCommonPrefix(["abcd","bcd","cd"]), "")

    def test_common_prefix_with_different_lengths(self):
        self.assertEqual(self.solution.longestCommonPrefix(["abc","ab","abcd"]), "ab")

    def test_empty_string_in_list(self):
        self.assertEqual(self.solution.longestCommonPrefix(["abc","","abcd"]), "")

    def test_long_strings(self):
        self.assertEqual(self.solution.longestCommonPrefix(["a"*200, "a"*150+"b", "a"*100+"c"]), "a"*100)

    def test_max_input_size(self):
        self.assertEqual(self.solution.longestCommonPrefix(["a"] * 200), "a")

    def test_unicode_characters(self):
        self.assertEqual(self.solution.longestCommonPrefix(["ünicode","ünivers","ünique"]), "üni")

    def test_case_sensitivity(self):
        self.assertEqual(self.solution.longestCommonPrefix(["Apple","app","application"]), "")

if __name__ == '__main__':
    unittest.main()
