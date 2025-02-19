arr = [2,3,6,7]
target = 7

def combination_sum(idx, n, arr, target, ds, res):
    # TC: O(2^t * k), SC: O(k * x)
    if idx == n:
        if target == 0:
            res.append(ds.copy())
        return

    if arr[idx] <= target:
        ds.append(arr[idx])
        combination_sum(idx, n, arr, target - arr[idx], ds, res)
        ds.pop()
    combination_sum(idx + 1, n, arr, target, ds, res)

res = []
combination_sum(0, len(arr), arr, target, [], res)
print(res)


