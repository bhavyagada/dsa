def get_subset_sums(idx, arr, n, sum, ans):
    if idx == n:
        ans.append(sum)
        return
    
    get_subset_sums(idx + 1, arr, n, sum + arr[idx], ans)
    get_subset_sums(idx + 1, arr, n, sum, ans)

arr = [1,2,1]
n = len(arr)
sum = 0
ans = []
get_subset_sums(0, arr, n, sum, ans)
ans.sort()
print(ans)
assert ans == [0,1,1,2,2,3,3,4]
