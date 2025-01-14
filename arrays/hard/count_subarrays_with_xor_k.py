from collections import defaultdict

nums = [4, 2, 2, 6, 4]
k = 6

# similar to count subarrays with sum = 0
def count_subarrays(nums, k):
    # optimal => TC: O(n), SC: O(n)
    cnt = 0
    xr = 0
    hashmap = defaultdict(int)
    hashmap[xr] = 1 # count of 0
    for i in range(len(nums)):
        xr = xr ^ nums[i]
        x = xr ^ k
        cnt += hashmap[x]
        hashmap[xr] += 1
    return cnt
print(count_subarrays(nums, k))
