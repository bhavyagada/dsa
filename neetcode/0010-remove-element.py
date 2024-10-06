import unittest
from typing import List

class Solution:
    """
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val: 
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                n -= 1
            else: i += 1
        return n

class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 2)
        self.assertCountEqual(nums[:k], [2, 2])

    def test_example_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 5)
        self.assertCountEqual(nums[:k], [0, 1, 3, 0, 4])

    def test_empty_array(self):
        nums = []
        val = 0
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums, [])

    def test_all_elements_removed(self):
        nums = [1, 1, 1]
        val = 1
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 0)

    def test_no_elements_removed(self):
        nums = [1, 2, 3, 4, 5]
        val = 6
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 5)
        self.assertCountEqual(nums[:k], [1, 2, 3, 4, 5])

    def test_max_length_array(self):
        nums = list(range(100))  # 0 to 99
        val = 50
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 99)
        self.assertNotIn(50, nums[:k])

    def test_min_length_array(self):
        nums = [0]
        val = 0
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 0)

    def test_max_value(self):
        nums = [50, 50, 50]
        val = 50
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 0)

    def test_min_value(self):
        nums = [0, 0, 0]
        val = 0
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 0)

    def test_mixed_values(self):
        nums = [0, 50, 25, 50, 0]
        val = 50
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 3)
        self.assertCountEqual(nums[:k], [0, 25, 0])

if __name__ == '__main__':
    unittest.main()
