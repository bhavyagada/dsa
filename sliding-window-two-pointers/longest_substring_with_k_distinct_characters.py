from collections import defaultdict
s = "aaabbccd"
k = 2

def longest_substring_brute(s, k):
    # brute => TC: O(n^2), SC: O(256)
    n, max_len = len(s), 0
    mpp = defaultdict(int)
    for i in range(n):
        mpp.clear()
        for j in range(i, n):
            mpp[s[j]] += 1
            if len(mpp) <= k:
                max_len = max(max_len, j - i + 1)
            else:
                break
    return max_len
print("brute", longest_substring_brute(s, k))

def longest_substring_optimal(s, k):
    # optimal => TC: O(n), SC: O(256)
    n = len(s)
    left, max_len = 0, 0
    mpp = defaultdict(int)
    for right in range(n):
        mpp[s[right]] += 1
        if len(mpp) <= k:
            max_len = max(max_len, right - left + 1)
        else:
            mpp[s[left]] -= 1
            if mpp[s[left]] == 0: mpp.pop(s[left])
            left += 1
    return max_len
print("optimal", longest_substring_optimal(s, k))
