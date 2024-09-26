from typing import List

class Solution:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    
    You must write an algorithm that runs in O(n) time and without using the division operation.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n): res[i] = res[i - 1] * nums[i - 1]
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

arr = [-1, 1, 0, -3, 3]
solution = Solution()
print(solution.productExceptSelf(arr))
