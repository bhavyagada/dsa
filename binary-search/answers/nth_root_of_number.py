n = 3
m = 27

def nth_root(n, m):
    # optimal => TC: O(nlogn), SC: O(1)
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        midN = mid ** n
        if midN == m:
            return mid
        elif midN < m:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(nth_root(n, m))
