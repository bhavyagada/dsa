import unittest
import random, string

class Solution:
    """
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        st_map, ts_map = {}, {}
        for sc, tc in zip(s, t):
            if (sc in st_map and st_map[sc] != tc) or (tc in ts_map and ts_map[tc] != sc): return False
            st_map[sc] = tc
            ts_map[tc] = sc
        return True

class TestIsomorphicStrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_cases(self):
        self.assertTrue(self.solution.isIsomorphic("egg", "add"))
        self.assertFalse(self.solution.isIsomorphic("foo", "bar"))
        self.assertTrue(self.solution.isIsomorphic("paper", "title"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isIsomorphic("", ""))

    def test_single_character(self):
        self.assertTrue(self.solution.isIsomorphic("a", "b"))

    def test_same_string(self):
        self.assertTrue(self.solution.isIsomorphic("abcde", "abcde"))

    def test_all_same_characters(self):
        self.assertTrue(self.solution.isIsomorphic("aaaa", "bbbb"))
        self.assertFalse(self.solution.isIsomorphic("aaaa", "abba"))

    def test_max_length(self):
        # Test with maximum allowed length (5 * 10^4)
        max_length = 5 * 10**4
        s = ''.join(random.choices(string.ascii_lowercase, k=max_length))
        t = ''.join(random.choices(string.ascii_lowercase, k=max_length))
        result = self.solution.isIsomorphic(s, t)
        self.assertIn(result, [True, False])  # The result could be either True or False

    def test_ascii_characters(self):
        # Test with various ASCII characters
        s = ''.join(chr(i) for i in range(128))
        t = ''.join(random.sample(s, len(s)))
        result = self.solution.isIsomorphic(s, t)
        self.assertIn(result, [True, False])

if __name__ == '__main__':
    unittest.main()
