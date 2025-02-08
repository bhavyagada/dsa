from collections import defaultdict
nums = [1,2,1,2,3]
k = 2

def count_subarrays_brute(nums, k):
    # brute => TC: O(n^2), SC: O(n)
    n = len(nums)
    cnt = 0
    for i in range(n):
        mpp = defaultdict(int)
        for j in range(i, n):
            mpp[nums[j]] += 1
            if (len(mpp) == k): cnt += 1
            elif (len(mpp) > k): break
    return cnt
print("brute", count_subarrays_brute(nums, k))

def count_subarrays_optimal(nums, k):
    # optimal => TC: O(2 x 2n), SC: O(n)
    if (k < 0): return 0
    n = len(nums)
    left, cnt = 0, 0
    mpp = defaultdict(int)
    for right in range(n):
        mpp[nums[right]] += 1
        while (len(mpp) > k):
            mpp[nums[left]] -= 1
            if mpp[nums[left]] == 0: 
                mpp.pop(nums[left])
            left += 1
        cnt += (right - left + 1)
    return cnt
leq_k = count_subarrays_optimal(nums, k)
leq_k_1 = count_subarrays_optimal(nums, k - 1)
print("optimal", leq_k - leq_k_1)
