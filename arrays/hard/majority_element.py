nums = [1,2,2,3,2,1,1,3]

def majority_element(nums):
    # optimal => TC: O(2n), SC: O(1)
    el1, el2 = None, None
    cnt1, cnt2 = 0, 0
    for i in range(len(nums)):
        if cnt1 == 0 and el2 != nums[i]:
            el1 = nums[i]
            cnt1 = 1
        elif cnt2 == 0 and el1 != nums[i]:
            el2 = nums[i]
            cnt2 = 1
        elif nums[i] == el1:
            cnt1 += 1
        elif nums[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    
    mini = len(nums) // 3
    res = []
    cnt1, cnt2 = 0, 0
    for i in range(len(nums)):
        if nums[i] == el1: cnt1 += 1
        if nums[i] == el2: cnt2 += 1
    if cnt1 > mini: res.append(el1)
    if cnt2 > mini: res.append(el2)
    return res
print(majority_element(nums))
