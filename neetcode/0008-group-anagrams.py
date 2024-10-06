import unittest
from typing import List
from collections import defaultdict

class Solution:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s: counts[ord(c) - ord('a')] += 1
            anagrams[tuple(counts)].append(s)
        return list(anagrams.values())

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertAnagramGroupsEqual(self, actual, expected):
        self.assertEqual(len(actual), len(expected))
        actual_sorted = [sorted(group) for group in actual]
        expected_sorted = [sorted(group) for group in expected]
        self.assertEqual(sorted(actual_sorted), sorted(expected_sorted))

    def test_example_1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
        self.assertAnagramGroupsEqual(self.solution.groupAnagrams(strs), expected)

    def test_example_2(self):
        strs = [""]
        expected = [[""]]
        self.assertAnagramGroupsEqual(self.solution.groupAnagrams(strs), expected)

    def test_example_3(self):
        strs = ["a"]
        expected = [["a"]]
        self.assertAnagramGroupsEqual(self.solution.groupAnagrams(strs), expected)

    def test_empty_list(self):
        self.assertEqual(self.solution.groupAnagrams([]), [])

    def test_all_unique(self):
        strs = ["abc", "def", "ghi"]
        expected = [["abc"], ["def"], ["ghi"]]
        self.assertAnagramGroupsEqual(self.solution.groupAnagrams(strs), expected)

    def test_all_same(self):
        strs = ["aaa", "aaa", "aaa"]
        expected = [["aaa", "aaa", "aaa"]]
        self.assertAnagramGroupsEqual(self.solution.groupAnagrams(strs), expected)

    def test_max_length(self):
        strs = ["a" * 100, "a" * 100, "b" * 100]
        expected = [["a" * 100, "a" * 100], ["b" * 100]]
        self.assertAnagramGroupsEqual(self.solution.groupAnagrams(strs), expected)

    def test_max_input_size(self):
        strs = ["a"] * 10000 + ["b"] * 4
        expected = [["a"] * 10000, ["b"] * 4]
        self.assertAnagramGroupsEqual(self.solution.groupAnagrams(strs), expected)

    def test_mixed_lengths(self):
        strs = ["abc", "cb", "cba", "bca", "a", "c"]
        expected = [["abc", "cba", "bca"], ["cb"], ["a"], ["c"]]
        self.assertAnagramGroupsEqual(self.solution.groupAnagrams(strs), expected)

if __name__ == '__main__':
    unittest.main()
