arr = [5,6,7]

def subset_sums(i, n, arr, total, res):
    # TC: O(2^n), SC: O(n)
    if i == n:
        res.append(total)
        return
    
    subset_sums(i+1, n, arr, total+arr[i], res)
    subset_sums(i+1, n, arr, total, res)

res = []
subset_sums(0, len(arr), arr, 0, res)
print(sorted(res))

