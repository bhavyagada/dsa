from collections import defaultdict
s = "AABABBA"
k = 1

def longest_repeating_brute(s, k):
    # brute => TC: O(n^2), SC: O(26)
    n = len(s)
    max_len = 0
    for i in range(n):
        mpp = defaultdict(int)
        maxf = 0
        for j in range(i, n):
            mpp[ord(s[j]) - ord('A')] += 1
            maxf = max(maxf, mpp[ord(s[j]) - ord('A')])
            changes = (j - i + 1) - maxf
            if changes <= k:
                max_len = max(max_len, j - i + 1)
            else: break
    return max_len
print("brute", longest_repeating_brute(s, k))

def longest_repeating_optimal(s, k):
    # optimal => TC: O(n), SC: O(26)
    n = len(s)
    left, max_len, max_freq = 0, 0, 0
    mpp = defaultdict(int)
    for right in range(n):
        mpp[ord(s[right]) - ord('A')] += 1
        max_freq = max(max_freq, mpp[ord(s[right]) - ord('A')])
        if (right - left + 1) - max_freq > k:
            mpp[ord(s[left]) - ord('A')] -= 1
            left += 1
            continue
        max_len = max(max_len, right - left + 1)
    return max_len
print("optimal", longest_repeating_optimal(s, k))
