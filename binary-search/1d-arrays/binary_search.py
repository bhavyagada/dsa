nums = [-1,0,3,5,9,12]
target = 12

def search(nums, target):
    # optimal => TC: O(logn), SC: O(1)
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(search(nums, target))
