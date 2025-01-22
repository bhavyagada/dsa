arr = [7,7,7,7,13,11,12,7]
m = 2
k = 3

def count(day, arr, k):
    cnt, no_of_bouquets = 0, 0
    for i in range(len(arr)):
        if arr[i] <= day:
            cnt += 1
        else:
            no_of_bouquets += (cnt // k)
            cnt = 0
    no_of_bouquets += (cnt // k)
    return no_of_bouquets

def minimum_days_to_make_bouquets(arr, m, k):
    # optimal => TC: O(n*log(max-min)), SC: O(1)
    if (m * k) > len(arr): return -1

    low, high = float('inf'), float('-inf')
    for i in arr:
        low = min(low, i)
        high = max(high, i)

    while low <= high:
        mid = low + (high - low) // 2
        total = count(mid, arr, k)
        if total < m:
            low = mid + 1
        else:
            high = mid - 1
    return low
print(minimum_days_to_make_bouquets(arr, m, k))
