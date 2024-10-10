def generate_permutations(idx, nums, n, ans):
    if idx == n:
        ans.append(nums[:])
        return
    
    for i in range(idx, n):
        nums[idx], nums[i] = nums[i], nums[idx]
        generate_permutations(idx+1, nums, n, ans)
        nums[idx], nums[i] = nums[i], nums[idx]
    
nums = [1,2,3]
n = len(nums)
ans = []
generate_permutations(0, nums, n, ans)
print(ans)
assert sorted(ans) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
