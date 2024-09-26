from typing import List

class Solution:
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for n in numbers:
            if n - 1 not in numbers:
                length = 1
                while n + length in numbers: length += 1
                longest = max(longest, length)
        return longest

arr = [100, 4, 200, 1, 3, 2]
solution = Solution()
print(solution.longestConsecutive(arr))
