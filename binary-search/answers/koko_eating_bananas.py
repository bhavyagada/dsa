nums = [7,15,6,3,8]
h = 8
nums = [3,6,7,11]
h = 8

def can_eat(mid, nums, h):
    cnt = 0
    for i in nums:
        cnt = cnt + (-(i // -mid))
    return cnt

def koko_eating_bananas(nums, h):
    # optimal => TC: O(nlogn), SC: O(1)
    low, high = 0, float('-inf')
    for i in nums:
        high = max(high, i)

    while low <= high:
        mid = low + (high - low) // 2
        per_hour = can_eat(mid, nums, h)
        if per_hour <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low
print(koko_eating_bananas(nums, h))
