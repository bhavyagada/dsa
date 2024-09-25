import unittest
from typing import List

class Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        diff_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in diff_map: return [diff_map[diff], i]
            diff_map[n] = i

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertCountEqual(self.solution.twoSum([2,7,11,15], 9), [0,1])

    def test_example_2(self):
        self.assertCountEqual(self.solution.twoSum([3,2,4], 6), [1,2])

    def test_example_3(self):
        self.assertCountEqual(self.solution.twoSum([3,3], 6), [0,1])

    def test_negative_numbers(self):
        self.assertCountEqual(self.solution.twoSum([-1,-2,-3,-4,-5], -8), [2,4])

    def test_zero_sum(self):
        self.assertCountEqual(self.solution.twoSum([-1,0,1], 0), [0,2])

    def test_large_numbers(self):
        self.assertCountEqual(self.solution.twoSum([1000000000,1000000000], 2000000000), [0,1])

    def test_small_numbers(self):
        self.assertCountEqual(self.solution.twoSum([-1000000000,-1000000000], -2000000000), [0,1])

    def test_long_array(self):
        nums = list(range(10000))
        nums.append(10000)
        self.assertCountEqual(self.solution.twoSum(nums, 19999), [9999,10000])

    def test_first_and_last(self):
        self.assertCountEqual(self.solution.twoSum([1,2,3,4,5], 6), [1,3])

    def test_same_number_different_indices(self):
        self.assertCountEqual(self.solution.twoSum([3,3], 6), [0,1])

    def test_unsorted_array(self):
        self.assertCountEqual(self.solution.twoSum([4,2,1,5,3], 7), [1,3])

if __name__ == '__main__':
    unittest.main()
