nums = [2,3,1,4,1,1,1,2]

def jump_game_recursive(idx, jumps, nums):
    # brute => TC: O(n^n), SC: O(n)
    if idx >= len(nums) - 1: return jumps
    mini = float('inf')
    for i in range(1, nums[idx] + 1):
        mini = min(mini, jump_game_recursive(idx + i, jumps + 1, nums))
    return mini
print("recursive: ", jump_game_recursive(0, 0, nums))

def jump_game_dp(idx, jumps, nums, dp):
    # better => TC: O(n^2), SC: O(n^2)
    if idx >= len(nums) - 1: return jumps
    if dp[idx][jumps] != -1: return dp[idx][jumps]
    mini = float('inf')
    for i in range(1, nums[idx] + 1):
        mini = min(mini, jump_game_dp(idx + i, jumps + 1, nums, dp))
    dp[idx][jumps] = mini
    return mini
n = len(nums)
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
print("recursive dp: ", jump_game_dp(0, 0, nums, dp))

def jump_game(nums):
    # optimal => TC: O(n), SC: (1)
    n = len(nums)
    jumps = 0
    left, right = 0, 0
    while right < n - 1:
        farthest = 0
        for i in range(left, right + 1):
            farthest = max(farthest, i + nums[i])
        left = right + 1
        right = farthest
        jumps += 1
    return jumps
print("optimal: ", jump_game(nums))


