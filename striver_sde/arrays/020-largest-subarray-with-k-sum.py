def largest_subarray(nums):
    n = len(nums)
    mpp = {}
    max_len = 0
    sum = 0
    for i in range(n):
        sum += nums[i]
        if sum == 0:
            max_len = i + 1
        else:
            if sum in mpp:
                max_len = max(max_len, i - mpp[sum])
            else:
                mpp[sum] = i
    return max_len

nums = [9,-3,3,-1,6,-5]
max_len = largest_subarray(nums)
print(max_len)
assert max_len == 5
