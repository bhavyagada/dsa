def generate_combinations(idx, nums, n, ds, ans, target):
    if target == 0:
        ans.append(ds.copy())
        return
    
    for i in range(idx, n):
        if i != idx and nums[i] == nums[i-1]: continue
        if nums[i] > target: break

        ds.append(nums[i])
        generate_combinations(i+1, nums, n, ds, ans, target-nums[i])
        ds.pop()

candidates = [10,1,2,7,6,1,5]
candidates.sort()
target = 8
n = len(candidates)
ans = []
generate_combinations(0, candidates, n, [], ans, target)
print(ans)
assert ans == [[1,1,6],[1,2,5],[1,7],[2,6]]
