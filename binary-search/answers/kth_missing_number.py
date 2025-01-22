arr = [4,7,9,10]
k = 1

def find_missing_number(arr, k):
    # brute force => TC: O(n), SC: O(1)
    # for i in range(len(arr)):
    #     if arr[i] <= k: k += 1
    #     else: break
    # return k

    # optimal => TC: O(logn), SC: O(1)
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        missing = arr[mid] - mid - 1
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    
    # result = arr[high] + more
    # missing = arr[high] - high - 1
    # more = k - missing = k - arr[high] + high + 1
    # result = arr[high] + more = k + high + 1 or low + k
    return low + k
print(find_missing_number(arr, k))
