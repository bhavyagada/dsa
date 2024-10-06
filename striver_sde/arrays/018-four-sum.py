def four_sum(nums, target):
    n = len(nums)
    ans = []
    nums.sort()
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(i + 1, n):
            if j > i+1 and nums[j] == nums[j-1]: continue

            k = j + 1
            l = n - 1
            while k < l:
                _sum = nums[i] + nums[j] + nums[k] + nums[l]
                if _sum == target:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1

                    while k < l and nums[k] == nums[k-1]: k += 1
                    while k < l and nums[l] == nums[l+1]: l -= 1
                elif _sum < target:
                    k += 1
                else:
                    l -= 1
    return ans

nums = [1,0,-1,0,-2,2]
target = 0
ans = four_sum(nums, target)
print(ans)
assert ans == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]