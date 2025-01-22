arr = [1,2,3,4,5]
limit = 9

def is_min(mid, arr, limit):
    _sum = 0
    for n in arr:
        _sum += -(n // -mid)
    return _sum <= limit

def smallest_divisor(arr, limit):
    if len(arr) > limit: return -1
    low, high = 1, 0
    for i in arr:
        if i > high: high = i

    while low <= high:
        mid = low + (high - low) // 2
        if is_min(mid, arr, limit):
            high = mid - 1
        else:
            low = mid + 1
    return low
print(smallest_divisor(arr, limit))
