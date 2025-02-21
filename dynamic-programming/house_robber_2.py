nums = [2,7,9,3,1]

def robber(nums):
    # TC: O(2n), SC: O(1)
    n = len(nums)
    if n == 1: return nums[0]
    prev2, prev = 0, nums[0]
    for i in range(1, n):
        pick = nums[i]
        if i > 1: pick += prev2
        not_pick = prev
        curr = max(pick, not_pick)
        prev2 = prev
        prev = curr
    return prev
no_first = robber(nums[:-1])
no_last = robber(nums[1:])
print(max(no_first, no_last))

