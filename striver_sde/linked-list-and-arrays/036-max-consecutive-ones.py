def find_max_consecutive_ones(nums):
    max_ones, ones = 0, 0
    for n in nums:
        if n == 1:
            ones += 1
            max_ones = max(max_ones, ones)
        else:
            ones = 0

    return max_ones

nums = [1,1,0,1,1,1]
ans = find_max_consecutive_ones(nums)
print(ans)
assert ans == 3
