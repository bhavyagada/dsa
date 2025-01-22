arr = [0,3,4,7,10,9]
k = 4

def can_place(dist, arr, k):
    n = len(arr)
    cows = 1
    last = arr[0]
    for i in range(1, n):
        if arr[i] - last >= dist:
            cows += 1
            last = arr[i]
        if cows >= k: return True
    return False

def aggresive_cows(arr, k):
    # optimal => TC: O(nlogn) + O(n*log(max-min)), SC: O(1)
    arr.sort()
    n = len(arr)
    low, high = 1, arr[n-1] - arr[0]
    while low <= high:
        mid = low + (high - low) // 2
        if can_place(mid, arr, k):
            low = mid + 1
        else:
            high = mid - 1
    return high
print(aggresive_cows(arr, k))
