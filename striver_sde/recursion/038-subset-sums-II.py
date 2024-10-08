def generate_subsets(idx, arr, n, ds, ans):
    ans.append(ds.copy())
    for i in range(idx, n):
        if i != idx and arr[i] == arr[i-1]: continue
        ds.append(arr[i])
        generate_subsets(i+1, arr, n, ds, ans)
        ds.pop()

arr = [1,2,2]
arr.sort()
ans = []
generate_subsets(0, arr, len(arr), [], ans)
print(ans)
assert ans == [[],[1],[1,2],[1,2,2],[2],[2,2]]
