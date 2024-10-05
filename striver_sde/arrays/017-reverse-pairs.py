def merge(nums, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1
    
    while left <= mid:
        temp.append(nums[left])
        left += 1
    
    while right <= high:
        temp.append(nums[right])
        right += 1
    
    for i in range(low, high + 1):
        nums[i] = temp[i - low]

def count_pairs(nums, low, mid, high):
    count = 0
    j = mid + 1
    for i in range(low, mid + 1):
        while j <= high and nums[i] > 2 * nums[j]:
            j += 1
        count += (j - (mid + 1))
    return count

def merge_sort(nums, low, high):
    count = 0
    if low >= high: return count
    mid = (low + high) // 2
    count += merge_sort(nums, low, mid)
    count += merge_sort(nums, mid + 1, high)
    count += count_pairs(nums, low, mid, high)
    merge(nums, low, mid, high)
    return count

nums = [1,3,2,3,1]
count = merge_sort(nums, 0, len(nums) - 1)
print(count)
assert count == 2