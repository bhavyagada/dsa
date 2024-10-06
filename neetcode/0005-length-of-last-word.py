import unittest

class Solution:
    """
    Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.
    """
    def lengthOfLastWord(self, s: str) -> int:
        counts = 0
        for c in reversed(s):
            if c == " ":
                if counts >= 1: return counts
            else: counts += 1
        return counts

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello World"), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.lengthOfLastWord("   fly me   to   the moon  "), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.lengthOfLastWord("luffy is still joyboy"), 6)

    def test_single_word(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello"), 5)

    def test_single_letter(self):
        self.assertEqual(self.solution.lengthOfLastWord("a"), 1)

    def test_trailing_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello World  "), 5)

    def test_leading_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("  Hello"), 5)

    def test_multiple_spaces_between_words(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello   World"), 5)

    def test_all_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("    "), 0)

    def test_long_last_word(self):
        self.assertEqual(self.solution.lengthOfLastWord("This is a verylongword"), 12)

    def test_max_length_string(self):
        self.assertEqual(self.solution.lengthOfLastWord("a" * 10000), 10000)

    def test_mixed_case(self):
        self.assertEqual(self.solution.lengthOfLastWord("HeLLo WoRLD"), 5)

if __name__ == '__main__':
    unittest.main()
