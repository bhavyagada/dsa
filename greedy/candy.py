arr = [0,2,4,3,2,1,1,3,5,6,4,0,0]

def min_candies_brute(arr):
    # brute => TC: O(3n), SC: O(2n)
    n = len(arr)
    left, right = [0] * n, [0] * n
    left[0], right[n-1] = 1, 1

    for i in range(1, n):
        if arr[i] > arr[i-1]: left[i] = left[i-1] + 1
        else: left[i] = 1
    
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]: right[i] = right[i+1] + 1
        else: right[i] = 1

    mini = 0
    for i in range(n):
        mini += max(left[i], right[i])

    return mini
print("brute: ", min_candies_brute(arr))

def min_candies_better(arr):
    # better => TC: O(2n), SC: O(n)
    n = len(arr)
    left = [0] * n
    left[0] = 1

    for i in range(1, n):
        if arr[i] > arr[i-1]: left[i] = left[i-1] + 1
        else: left[i] = 1

    mini = max(left[n-1], 1)
    curr, right = 1, 1
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]: curr, right = right + 1, curr
        else: curr = 1
        mini += max(left[i], curr)
    return mini
print("better: ", min_candies_better(arr))

def min_candies_optimal(arr):
    # optimal => TC: O(n), SC: O(1)
    n = len(arr)
    mini, i = 1, 1
    while i < n:
        if arr[i] == arr[i-1]:
            mini += 1
            i += 1
            continue
        peak = 1
        while i < n and arr[i] > arr[i-1]:
            peak += 1
            mini += peak
            i += 1
        down = 1
        while i < n and arr[i] < arr[i-1]:
            mini += down
            i += 1
            down += 1
        if down > peak:
            mini += (down - peak)
    return mini
print("optimal: ", min_candies_optimal(arr))


