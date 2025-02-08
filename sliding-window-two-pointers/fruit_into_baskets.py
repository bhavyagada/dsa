from collections import defaultdict
arr = [3,1,2,2,2,2]

def longest_subarray(arr):
    n = len(arr)
    left, max_len = 0, 0
    mpp = defaultdict(int)
    for right in range(n):
        mpp[arr[right]] += 1
        if len(mpp) <= 2:
            max_len = max(max_len, right - left + 1)
        else:
            mpp[arr[left]] -= 1
            if mpp[arr[left]] == 0: mpp.pop(arr[left])
            left += 1
    return max_len
print(longest_subarray(arr))
