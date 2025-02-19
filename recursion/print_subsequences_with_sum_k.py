arr = [2,2,1,3]
k = 4

def subsequences_with_sum_k(i, n, arr, ds, total, k):
    # optimal => TC: O(2^n), SC: O(n)
    if i >= n:
        if total == k:
            print(ds)
        return
    ds.append(arr[i])
    subsequences_with_sum_k(i+1, n, arr, ds, total+arr[i], k)
    ds.remove(arr[i])
    subsequences_with_sum_k(i+1, n, arr, ds, total, k)
print("print all subsequences with sum k")
subsequences_with_sum_k(0, len(arr), arr, [], 0, k)
print()

def one_subsequence_with_sum_k(i, n, arr, ds, total, k):
    # optimal => TC: O(2^n), SC: O(n)
    if i >= n:
        if total == k:
            print(ds)
            return True
        else: return False
    ds.append(arr[i])
    if one_subsequence_with_sum_k(i+1, n, arr, ds, total+arr[i], k): return True
    ds.remove(arr[i])
    if one_subsequence_with_sum_k(i+1, n, arr, ds, total, k): return True
    return False
print("print any one subsequence with sum k")
one_subsequence_with_sum_k(0, len(arr), arr, [], 0, k)
print()

def count_subsequences_with_sum_k(i, n, arr, total, k):
    # optimal => TC: O(2^n), SC: O(n)
    if i >= n:
        if total == k:
            return 1
        return 0
    left = count_subsequences_with_sum_k(i+1, n, arr, total+arr[i], k)
    right = count_subsequences_with_sum_k(i+1, n, arr, total, k)
    return left + right
print("count of subsequences with sum k")
print(count_subsequences_with_sum_k(0, len(arr), arr, 0, k))


