arr = [1,3,2,3,1]

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def count_pairs(arr, low, mid, high):
    cnt = 0
    j = mid + 1
    for i in range(low, mid + 1):
        while j <= high and arr[i] > 2 * arr[j]:
            j += 1
        cnt += (j - (mid + 1))
    return cnt

def merge_sort(arr, low, high):
    # optimal => TC: O(2nlogn), SC: O(n)
    cnt = 0
    if low >= high: return cnt
    mid = (low + high) // 2
    cnt += merge_sort(arr, low, mid)
    cnt += merge_sort(arr, mid + 1, high)
    cnt += count_pairs(arr, low, mid, high)
    merge(arr, low, mid, high)
    return cnt

print(merge_sort(arr, 0, len(arr) - 1))
print(arr)
