nums = [4,5,6,7,0,1,2]
target = 0

def search_rotated_1(nums, target):
    # optimal => TC: O(logn), SC: O(1)
    idx = -1
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target: return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return idx
print("search in rotated sorted array:", search_rotated_1(nums, target))

nums = [2,5,6,0,0,1,2]
target = 2
def search_rotated_2(nums, target):
    # optimal => TC: O(logn), SC: O(1)
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target: return True
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return False
print("search in rotated sorted array (with duplicates)", search_rotated_2(nums, target))
