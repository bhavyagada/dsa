nums = [4,5,6,7,0,1,2,3]

def no_of_times_rotated(nums):
    # optimal => TC: O(logn), SC: O(1)
    n = len(nums)
    ans = float('inf')
    low, high = 0, n - 1
    index = -1
    while low <= high:
        mid = (low + high) // 2
        # if entire array sorted, don't perform BS
        if nums[low] <= nums[high]:
            if nums[low] < ans:
                index = low
                ans = nums[low]
            break

        if nums[low] <= nums[mid]:
            if nums[low] < ans:
                index = low
                ans = nums[low]
            low = mid + 1
        else:
            if nums[mid] < ans:
                index = mid
                ans = nums[mid]
            high = mid - 1
    return index
print(no_of_times_rotated(nums))
