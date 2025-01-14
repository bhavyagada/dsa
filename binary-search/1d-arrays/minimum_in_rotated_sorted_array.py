nums = [4,5,6,7,0,1,2,3]

def find_minimum(nums):
    # optimal => TC: O(logn), SC: O(1)
    n = len(nums)
    _min = float('inf')
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        # if entire array sorted, don't perform BS
        if nums[low] <= nums[high]:
            _min = min(_min, nums[low])
            break

        if nums[low] <= nums[mid]:
            _min = min(_min, nums[low])
            low = mid + 1
        else:
            _min = min(_min, nums[mid])
            high = mid - 1
    return _min
print(find_minimum(nums))
