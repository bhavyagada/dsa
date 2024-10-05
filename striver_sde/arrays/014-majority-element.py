def majority_element(nums):
    n = len(nums)
    el = None
    cnt = 0
    for i in range(n):
        if cnt == 0:
            el = nums[i]
            cnt += 1
        elif el == nums[i]:
            cnt += 1
        else:
            cnt -= 1
    return el

nums = [2,2,1,1,1,2,2]
el = majority_element(nums)
print(el)
assert el == 2
