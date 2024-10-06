from typing import List
from collections import defaultdict

class Solution:
    """
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        frequency = [[] for i in range(len(nums) + 1)]
        for n in nums: counts[n] += 1
        for n, c in counts.items(): frequency[c].append(n)

        res = []
        for i in range(len(frequency) - 1, -1, -1):
            for n in frequency[i]:
                res.append(n)
                k -= 1
                if k == 0: return res
