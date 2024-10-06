import unittest
from typing import List

class Solution:
    """
    Given an integer numRows, return the first numRows of Pascal's triangle.
    """
    def nCr(self, n: int, r: int) -> int:
        res = 1
        for i in range(r):
            res *= (n - i)
            res //= (i + 1)
        return int(res)

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for row in range(1, numRows + 1):
            temp = []
            for col in range(1, row + 1):
                temp.append(self.nCr(row - 1, col - 1))
            ans.append(temp)
        return ans

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        numRows = 5
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        self.assertEqual(self.solution.generate(numRows), expected)

    def test_example_2(self):
        numRows = 1
        expected = [[1]]
        self.assertEqual(self.solution.generate(numRows), expected)

    def test_two_rows(self):
        numRows = 2
        expected = [[1], [1, 1]]
        self.assertEqual(self.solution.generate(numRows), expected)

    def test_three_rows(self):
        numRows = 3
        expected = [[1], [1, 1], [1, 2, 1]]
        self.assertEqual(self.solution.generate(numRows), expected)

    def test_max_rows(self):
        # Only checking the length to ensure it generates up to the maximum constraint
        numRows = 30
        result = self.solution.generate(numRows)
        self.assertEqual(len(result), numRows)
        # Optionally check the last row for correctness
        expected_last_row = [1, 29, 406, 3654, 23751, 118755, 475020, 1560780, 4292145, 10015005, 20030010, 34597290, 51895935, 67863915, 77558760, 77558760, 67863915, 51895935, 34597290, 20030010, 10015005, 4292145, 1560780, 475020, 118755, 23751, 3654, 406, 29, 1]
        self.assertEqual(result[-1], expected_last_row)

if __name__ == '__main__':
    unittest.main()
