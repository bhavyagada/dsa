heights = [20,30,40,20]
n = len(heights)

# recursion
def frog_jump(i):
    # TC: O(2^n), SC: O(n)
    if i == 0: return 0
    left = frog_jump(i-1) + abs(heights[i] - heights[i-1])
    right = float('inf')
    if i > 1: right = frog_jump(i-2) + abs(heights[i] - heights[i-2])
    return min(left, right)
print("recursion: ", frog_jump(n-1))

# memoization
dp = [-1] * (n+1)
def frog_jump_memo(i, dp):
    # TC: O(n), SC: O(n) + O(n)
    if i == 0: return 0
    if dp[i] != -1: return dp[i]
    left = frog_jump_memo(i-1, dp) + abs(heights[i] - heights[i-1])
    right = float('inf')
    if i > 1: right = frog_jump_memo(i-2, dp) + abs(heights[i] - heights[i-2])
    dp[i] = min(left, right)
    return dp[i]
print("memoization: ", frog_jump_memo(n-1, dp))

# tabulation
def frog_jump_tab():
    # TC: O(n), SC: O(n)
    dp = [0] * n
    for i in range(1, n):
        left = dp[i-1] + abs(heights[i] - heights[i-1])
        right = float('inf')
        if i > 1: right = dp[i-2] + abs(heights[i] - heights[i-2])
        dp[i] = int(min(left, right))
    return dp[n-1]
print("tabulation: ", frog_jump_tab())

# space optimization
def frog_jump_optimal():
    # TC: O(n), SC: O(1)
    prev2, prev = 0, 0
    for i in range(1, n):
        left = prev + abs(heights[i] - heights[i-1])
        right = float('inf')
        if i > 1: right = prev2 + abs(heights[i] - heights[i-2])
        curr = int(min(left, right))
        prev2 = prev
        prev = curr
    return prev
print("space optimized: ", frog_jump_optimal())

# k steps
def frog_jump_k_steps(k):
    # TC: O(n), SC: O(n)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(1, k+1):
            if i-j >= 0:
                jump = dp[i-j] + abs(heights[i] - heights[i-j])
                dp[i] = min(dp[i], jump)
    return dp[n-1]
print("k jumps: ", frog_jump_k_steps(2))


