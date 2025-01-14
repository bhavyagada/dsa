nums = [9,-3,3,-1,6,-5]

def longest_subarray(nums):
    # optimal => TC: O(n), SC: O(n)
    n = len(nums)
    _max = 0
    _sum = 0
    hashmap = {}
    for i in range(n):
        _sum += nums[i]
        if _sum == 0:
            _max = i + 1
        else:
            if _sum in hashmap:
                _max = max(_max, i - hashmap[_sum])
            else:
                hashmap[_sum] = i
    return _max
print(longest_subarray(nums))
