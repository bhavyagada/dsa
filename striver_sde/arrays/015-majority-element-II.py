def majority_element(nums):
    n = len(nums)
    el1, el2 = None, None
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if cnt1 == 0 and el2 != nums[i]:
            el1 = nums[i]
            cnt1 = 1
        elif cnt2 == 0 and el1 != nums[i]:
            el2 = nums[i]
            cnt2 = 1
        elif el1 == nums[i]:
            cnt1 += 1
        elif el2 == nums[i]:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if el1 == nums[i]:
            cnt1 += 1
        if el2 == nums[i]:
            cnt2 += 1
    
    res = []
    if cnt1 > n//3: res.append(el1)
    if cnt2 > n//3: res.append(el2)
    
    return res

nums = [3,2,3]
res = majority_element(nums)
print(res)
assert res == [3]