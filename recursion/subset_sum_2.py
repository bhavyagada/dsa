nums = [1,2,2]

def subsets(idx, n, nums, ds, res):
    # TC: O(2^n * k), SC: O(2^n) + O(k) + O(n)
    res.append(ds.copy())
    for i in range(idx, n):
        if i > idx and nums[i] == nums[i-1]: continue
        ds.append(nums[i])
        subsets(i+1, n, nums, ds, res)
        ds.pop()

res = []
nums.sort()
subsets(0, len(nums), nums, [], res)
print(res)

