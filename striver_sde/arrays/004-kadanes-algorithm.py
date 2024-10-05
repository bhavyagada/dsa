def max_subarray_sum(nums, n):
    max_sum, sum = float('-inf'), 0
    ans_start, ans_end = -1, -1
    for i in range(n):
        if sum == 0: start = i
        sum += nums[i]
        if sum > max_sum:
            max_sum = sum
            ans_start = start
            ans_end = i
        if sum < 0: sum = 0
    return max_sum, nums[ans_start:ans_end+1]

nums = [5,4,-1,7,8]
n = len(nums)
print(max_subarray_sum(nums, n))