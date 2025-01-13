nums = [2,2,1,1,1,2,2]

def majority_element(nums):
    # optimal => TC: O(n), SC: O(1)
    el = None
    cnt = 0
    for n in nums:
        if cnt == 0:
            el = n
            cnt = 1
        elif n == el:
            cnt += 1
        else:
            cnt -= 1
    return el
print(majority_element(nums))
