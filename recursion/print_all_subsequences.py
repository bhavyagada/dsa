arr = [1,2,3]

def print_subsequences(idx, n, arr, ds):
    # optimal => TC: O(2^n), SC: O(n)
    if idx == n:
        print(ds)
        return
    ds.append(arr[idx])
    print_subsequences(idx + 1, n, arr, ds)
    ds.remove(arr[idx])
    print_subsequences(idx + 1, n, arr, ds)
print_subsequences(0, len(arr), arr, [])

