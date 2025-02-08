nums = [1,1,2,1,1]
k = 3

def subarray_sum_optimal(nums, goal):
    # optimal => TC: O(2 x 2n), SC: O(1)
    if goal < 0: return 0
    n = len(nums)
    left, cnt, total = 0, 0, 0
    for right in range(n):
        total += (nums[right] % 2)
        while total > goal:
            total -= (nums[left] % 2)
            left += 1
        cnt += (right - left + 1)
    return cnt
leq_goal = subarray_sum_optimal(nums, k)
leq_goal_minus_one = subarray_sum_optimal(nums, k - 1)
print(leq_goal - leq_goal_minus_one)
