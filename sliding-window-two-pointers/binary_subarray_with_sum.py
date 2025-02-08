nums = [1,0,1,0,1]
goal = 2

def subarray_sum_optimal(nums, goal):
    # optimal => TC: O(2 x 2n), SC: O(1)
    if goal < 0: return 0
    n = len(nums)
    left, cnt, total = 0, 0, 0
    for right in range(n):
        total += nums[right]
        while total > goal:
            total -= nums[left]
            left += 1
        cnt += (right - left + 1)
    return cnt
leq_goal = subarray_sum_optimal(nums, goal)
leq_goal_minus_one = subarray_sum_optimal(nums, goal - 1)
print(leq_goal - leq_goal_minus_one)
