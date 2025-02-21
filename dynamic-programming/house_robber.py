nums = [2,7,9,3,1]
n = len(nums)

def robber_recursion(ind):
    # TC: O(2^n), SC: O(n)
    if ind == 0: return nums[ind]
    if ind < 0: return 0
    pick = nums[ind] + robber_recursion(ind-2)
    not_pick = robber_recursion(ind-1)
    return max(pick, not_pick)
print("recursion: ", robber_recursion(n-1))

def robber_memo(ind, dp):
    # TC: O(n), SC: O(n) + O(n)
    if ind == 0: return nums[ind]
    if ind < 0: return 0
    if dp[ind] != -1: return dp[ind]
    pick = nums[ind] + robber_memo(ind-2, dp)
    not_pick = robber_memo(ind-1, dp)
    dp[ind] = max(pick, not_pick)
    return dp[ind]
dp = [-1] * (n+1)
print("memoization: ", robber_memo(n-1, dp))

def robber_tab():
    # TC: O(n), SC: O(n)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        pick = nums[i]
        if i > 1: pick += dp[i-2]
        not_pick = dp[i-1]
        dp[i] = max(pick, not_pick)
    return dp[n-1]
print("tabulation: ", robber_tab())

def robber_optimal():
    prev2, prev = 0, nums[0]
    for i in range(1, n):
        pick = nums[i]
        if i > 1: pick += prev2
        not_pick = prev
        curr = max(pick, not_pick)
        prev2 = prev
        prev = curr
    return prev
print("space optimized: ", robber_optimal())


