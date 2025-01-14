nums = [-1,0,1,2,-1,-4]

def three_sum(nums):
    # optimal => TC: O(nlogn) + O(n^2), SC: O(1)
    nums.sort() # nlogn
    ans = []
    n = len(nums)
    for i in range(n): # n
        if i != 0 and nums[i-1] == nums[i]: continue
        
        j = i + 1
        k = n - 1
        while j < k: # n
            total_sum = nums[i] + nums[j] + nums[k]
            if total_sum == 0:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j-1]: j += 1
                while j < k and nums[k] == nums[k+1]: k -= 1
            elif total_sum < 0:
                j += 1
            elif total_sum > 0: 
                k -= 1
    return ans
print(three_sum(nums))
