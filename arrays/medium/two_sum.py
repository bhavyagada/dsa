nums = [2,7,11,15]
target = 9

def two_sum(nums, target):
    # TC: O(n), SC: O(n)
    hashmap = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[nums[i]] = i
print(two_sum(nums, target))
