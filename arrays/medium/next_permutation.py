nums = [2,1,5,4,3,0,0]

# next permutation (recursion)
def next_permutation_recursion(nums):
    ans = []
    def find_all_permutations(ind, nums, ans, n):
        # brute => TC: O(n! * n), SC: O(n)
        if ind == n:
            ans.append(nums[:])
            return

        for i in range(ind, n):
            nums[ind], nums[i] = nums[i], nums[ind]
            find_all_permutations(ind + 1, nums, ans, n)
            nums[ind], nums[i] = nums[i], nums[ind]
    find_all_permutations(0, nums, ans, len(nums))

    import itertools
    ans.sort()
    ans = list(k for k, _ in itertools.groupby(ans)) # dedup
    for i in range(len(ans) - 1):
        if ans[i] == nums:
            return ans[i+1]
    return ans[0]
print("next permutation (recursion):", next_permutation_recursion(nums))

# next permutation (iterative)
def next_permutation(nums):
    # optimal => TC: O(3n), SC: O(1)
    idx = -1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i+1]:
            idx = i
            break

    if idx == -1: return sorted(nums)

    for i in range(len(nums)-1, idx, -1):
        if nums[i] > nums[idx]:
            nums[i], nums[idx] = nums[idx], nums[i]
            break
    nums[idx+1:] = reversed(nums[idx+1:])
    return nums
print("next permutation (iterative):", next_permutation(nums))
