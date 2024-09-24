import unittest
from typing import List

class Solution:
    """
    Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1. After doing so, return the array.
    """
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        greatest = -1
        for i in range(n - 1, -1, -1):
            new_greatest = max(greatest, arr[i])
            arr[i] = greatest
            greatest = new_greatest
        return arr

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        arr = [17,18,5,4,6,1]
        expected = [18,6,6,6,1,-1]
        self.assertEqual(self.solution.replaceElements(arr), expected)

    def test_example_2(self):
        arr = [400]
        expected = [-1]
        self.assertEqual(self.solution.replaceElements(arr), expected)

    def test_all_ascending(self):
        arr = [1,2,3,4,5]
        expected = [5,5,5,5,-1]
        self.assertEqual(self.solution.replaceElements(arr), expected)

    def test_all_descending(self):
        arr = [5,4,3,2,1]
        expected = [4,3,2,1,-1]
        self.assertEqual(self.solution.replaceElements(arr), expected)

    def test_all_same(self):
        arr = [3,3,3,3,3]
        expected = [3,3,3,3,-1]
        self.assertEqual(self.solution.replaceElements(arr), expected)

    def test_two_elements(self):
        arr = [1,2]
        expected = [2,-1]
        self.assertEqual(self.solution.replaceElements(arr), expected)

    def test_large_array(self):
        arr = list(range(10000, 0, -1))
        expected = list(range(9999, 0, -1)) + [-1]
        self.assertEqual(self.solution.replaceElements(arr), expected)

    def test_max_values(self):
        arr = [100000, 1, 100000]
        expected = [100000, 100000, -1]
        self.assertEqual(self.solution.replaceElements(arr), expected)

    def test_min_values(self):
        arr = [1, 1, 1]
        expected = [1, 1, -1]
        self.assertEqual(self.solution.replaceElements(arr), expected)

if __name__ == '__main__':
    unittest.main()
