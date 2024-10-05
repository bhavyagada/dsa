def sort_colors(nums):
    n = len(nums)
    low, mid = 0, 0
    high = n - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1

nums = [2,0,0,2,1,2,0,2,1,0,2,0,1,2,0,1,0,2,0,1,0,2,0,1,0,2,0,1,2,0,1,2,2,1,1,0]
sort_colors(nums)
print(nums)