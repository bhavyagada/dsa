arr = [1,2,3]

def permutations(n, arr, mpp, ds, res):
    # TC: O(n! * n), SC: O(n) + O(n)
    if sum(mpp) == n:
        res.append(ds.copy())
        return

    for x in range(n):
        if not mpp[x]:
            mpp[x] = 1
            ds.append(arr[x])
            permutations(n, arr, mpp, ds, res)
            ds.pop()
            mpp[x] = 0

n = len(arr)
mpp = [0] * n
res = []
permutations(n, arr, mpp, [], res)
print("extra space: ", res)

def permutations_optimal(idx, n, arr, res):
    # optimal => TC: O(n! * n), SC: O(n)
    if idx == n:
        res.append(arr.copy())
        return

    for i in range(idx, n):
        arr[i], arr[idx] = arr[idx], arr[i]
        permutations_optimal(idx+1, n, arr, res)
        arr[i], arr[idx] = arr[idx], arr[i]

res = []
permutations_optimal(0, n, arr, res)
print("optimal: ", res)

