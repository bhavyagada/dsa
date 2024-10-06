def longest_consecutive_sequence(nums):
    arr = set(nums)
    max_cnt = 0
    for n in arr:
        if n - 1 not in arr:
            cnt = 1
            while n + cnt in arr:
                cnt += 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt

nums = [100,4,200,1,3,2]
longest = longest_consecutive_sequence(nums)
print(longest)
assert longest == 4
