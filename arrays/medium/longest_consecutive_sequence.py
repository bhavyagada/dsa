arr = [100,102,1,3,104,2,4,103,105,101]

def longest_consecutive_subsequence(arr):
    # optimal => TC: O(3n), SC: O(n)
    longest = 0
    nums = set()
    for i in arr: nums.add(i)

    for el in nums:
        if el - 1 not in nums:
            cnt = 1
            while el + cnt in nums:
                cnt += 1
            longest = max(longest, cnt)
    return longest
print(longest_consecutive_subsequence(arr))
