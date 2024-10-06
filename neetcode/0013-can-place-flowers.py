import unittest
from typing import List

class Solution:
    """
    You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
    """
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        for i in range(l):
            if (i == 0 or flowerbed[i - 1] == 0) and (flowerbed[i] == 0) and (i == (l - 1) or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
        return n <= 0

class TestCanPlaceFlowers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_cases(self):
        self.assertTrue(self.solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))
        self.assertFalse(self.solution.canPlaceFlowers([1, 0, 0, 0, 1], 2))

    def test_empty_flowerbed(self):
        self.assertTrue(self.solution.canPlaceFlowers([0, 0, 0, 0, 0], 3))
        self.assertFalse(self.solution.canPlaceFlowers([0, 0], 2))

    def test_full_flowerbed(self):
        self.assertFalse(self.solution.canPlaceFlowers([1, 1, 1, 1], 1))
        self.assertFalse(self.solution.canPlaceFlowers([1, 1], 1))

    def test_flowerbed_with_one_empty_plot(self):
        self.assertTrue(self.solution.canPlaceFlowers([1, 0, 1], 0))
        self.assertFalse(self.solution.canPlaceFlowers([1, 0, 1], 1))

    def test_flowerbed_with_multiple_empty_plots(self):
        self.assertTrue(self.solution.canPlaceFlowers([0, 0, 0], 2))
        self.assertFalse(self.solution.canPlaceFlowers([0, 0, 0, 0], 3))
        self.assertFalse(self.solution.canPlaceFlowers([0, 0, 0], 3))

    def test_flowerbed_with_adjacent_plots(self):
        self.assertFalse(self.solution.canPlaceFlowers([0, 1, 0], 1))
        self.assertFalse(self.solution.canPlaceFlowers([1, 0, 1], 1))

    def test_large_flowerbed(self):
        # Test with maximum allowed length (2 * 10^4)
        max_length = 2 * (10 ** 4)
        flowerbed = [0] * max_length
        n = max_length // 3
        # We should be able to plant n flowers
        self.assertTrue(self.solution.canPlaceFlowers(flowerbed[:max_length], n))

    def test_edge_cases_with_n_zero(self):
        # If n is zero we should always return true
        self.assertTrue(self.solution.canPlaceFlowers([0, 1, 0], 0))
        self.assertTrue(self.solution.canPlaceFlowers([1], 0))
        
if __name__ == '__main__':
    unittest.main()
