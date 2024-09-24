import unittest
from typing import List

class Solution:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset: return True
            hashset.add(n)
        return False

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.containsDuplicate([1,2,3,1]))

    def test_example_2(self):
        self.assertFalse(self.solution.containsDuplicate([1,2,3,4]))

    def test_example_3(self):
        self.assertTrue(self.solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

    def test_empty_array(self):
        self.assertFalse(self.solution.containsDuplicate([]))

    def test_single_element_array(self):
        self.assertFalse(self.solution.containsDuplicate([5]))

    def test_two_identical_elements(self):
        self.assertTrue(self.solution.containsDuplicate([7, 7]))

    def test_large_numbers(self):
        self.assertTrue(self.solution.containsDuplicate([1000000000, 1000000000]))

    def test_negative_numbers(self):
        self.assertTrue(self.solution.containsDuplicate([-1, -1, 2, 3]))

    def test_mixed_positive_and_negative(self):
        self.assertTrue(self.solution.containsDuplicate([-1, 1, 2, -1, -2, 3]))

    def test_all_unique_negative_numbers(self):
        self.assertFalse(self.solution.containsDuplicate([-3, -2, -1]))

    def test_zero_and_negative_zero(self):
        self.assertTrue(self.solution.containsDuplicate([0, -0, 1, 2]))

    def test_large_array_no_duplicates(self):
        self.assertFalse(self.solution.containsDuplicate(list(range(1, 100001))))

    def test_large_array_with_duplicates_at_ends(self):
        nums = list(range(1, 100000)) + [1]
        self.assertTrue(self.solution.containsDuplicate(nums))

if __name__ == '__main__':
    unittest.main()
