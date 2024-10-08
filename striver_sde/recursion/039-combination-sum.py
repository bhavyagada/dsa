def generate_combinations(idx, nums, n, ds, ans, target):
    if idx == n:
        if target == 0: ans.append(ds.copy())
        return
    
    if nums[idx] <= target:
        ds.append(nums[idx])
        generate_combinations(idx, nums, n, ds, ans, target - nums[idx])
        ds.pop()
    generate_combinations(idx + 1, nums, n, ds, ans, target)

candidates = [2,3,5]
target = 8
n = len(candidates)
ans = []
generate_combinations(0, candidates, n, [], ans, target)
print(ans)
assert ans == [[2,2,2,2],[2,3,3],[3,5]]
