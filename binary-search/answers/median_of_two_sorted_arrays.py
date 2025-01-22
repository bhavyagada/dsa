arr1 = [1,4,7,10,12]
arr2 = [2,3,6,15]

def find_median_brute(arr1, arr2):
    # brute => TC: O(n1+n2), SC: O(1)
    n1, n2 = len(arr1), len(arr2)
    n = n1 + n2
    idx2 = n // 2
    idx1 = idx2 - 1
    cnt = 0
    idx1el, idx2el = -1, -1
    
    i, j = 0, 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            if cnt == idx1:
                idx1el = arr1[i]
            if cnt == idx2:
                idx2el = arr1[i]
            cnt += 1
            i += 1
        else:
            if cnt == idx1:
                idx1el = arr2[j]
            if cnt == idx2:
                idx2el = arr2[j]
            cnt += 1
            j += 1
    while i < n1:
        if cnt == idx1:
            idx1el = arr1[i]
        if cnt == idx2:
            idx2el = arr1[i]
        cnt += 1
        i += 1
    while j < n2:
        if cnt == idx1:
            idx1el = arr2[j]
        if cnt == idx2:
            idx2el = arr2[j]
        cnt += 1
        j += 1

    if n % 2 == 1: return float(idx2el)
    return float(idx1el + idx2el) / 2.0
print("find median of 2 sorted arrays (brute force):", find_median_brute(arr1, arr2))

def find_median_optimal(a, b):
    # optimal => TC: O(log(min(n1,n2))), SC: O(1)
    n1, n2 = len(a), len(b)
    if n1 > n2: return find_median_optimal(b, a)

    n = n1 + n2
    left = (n1 + n2 + 1) // 2
    low, high = 0, n1
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
        if mid1 < n1:
            r1 = a[mid1]
        if mid2 < n2:
            r2 = b[mid2]
        if mid1 - 1 >= 0:
            l1 = a[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            if n % 2 == 1: return max(l1, l2)
            else: return (float(max(l1, l2)) - float(min(r1, r2))) / 2.0
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return None # dummy return
print("find median of 2 sorted arrays (optimal):", find_median_optimal(arr1, arr2))

def find_kth_element(a, b, k):
    # optimal => TC: O(log(min(n1,n2))), SC: O(1)
    n, m = len(a), len(b)
    if n > m: return find_kth_element(b, a, k)
    
    left = k
    low = max(0, k - m)
    high = min(k, n)
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
        if mid1 < n:
            r1 = a[mid1]
        if mid2 < m:
            r2 = b[mid2]
        if mid1 - 1 >= 0:
            l1 = a[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return None # dummy statement
print("find kth element:", find_kth_element(arr1, arr2, 2))

