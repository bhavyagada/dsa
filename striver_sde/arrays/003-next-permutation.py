def next_permutation(nums, n):
    pivot = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i+1]: 
            pivot = i
            break
    
    if pivot == -1: nums.reverse()
    else:
        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        
        nums[pivot+1:] = reversed(nums[pivot+1:])

nums = [2,1,5,4,3,0,0]
n = len(nums)
next_permutation(nums, n)
print(nums)