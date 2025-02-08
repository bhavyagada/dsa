nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

def max_ones(nums, k):
    n = len(nums)
    left, max_ones, zeros = 0, 0, 0
    for right in range(n):
        if nums[right] == 0: zeros += 1
        if zeros > k:
            if nums[left] == 0: zeros -= 1
            left += 1
        if zeros == k: 
            max_ones = max(max_ones, right - left + 1)
    return max_ones
print(max_ones(nums, k))
