arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

def minimum_platforms(arr, dep):
    # optimal => TC: O(2nlogn + 2n), SC: O(1)
    n = len(arr)
    arr.sort()
    dep.sort()
    a, d = 0, 0
    cnt, max_cnt = 0, 0
    while a < n:
        if arr[a] <= dep[d]:
            cnt += 1
            a += 1
        else:
            cnt -= 1
            d += 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt
print(minimum_platforms(arr, dep))

