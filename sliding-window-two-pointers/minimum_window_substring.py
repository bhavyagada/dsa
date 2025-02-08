from collections import defaultdict

s = "ADOBECODEBANC"
t = "ABC"

def minimum_window_substring_brute(s, t):
    # brute => TC: O(n^2), SC: O(128)
    n, m = len(s), len(t)
    min_len, sid = float('inf'), -1
    for i in range(n):
        mpp = [0] * 128
        for k in range(m): mpp[ord(t[k])] += 1
        cnt = 0
        for j in range(i, n):
            if mpp[ord(s[j])] > 0: cnt += 1
            mpp[ord(s[j])] -= 1
            if cnt == m:
                if (j - i + 1) < min_len:
                    min_len = j - i + 1
                    sid = i
                break
    return s[sid:sid+min_len] if sid != -1 else ""
print("brute", minimum_window_substring_brute(s, t))

def minimum_window_substring_optimal(s, t):
    # optimal => TC: O(2n) + O(m), SC: O(128)
    n, m = len(s), len(t)
    min_len = float('inf')
    sid, left, cnt = -1, 0, 0
    mpp = [0] * 128
    for i in range(m): mpp[ord(t[i])] += 1
    for right in range(n):
        if mpp[ord(s[right])] > 0: cnt += 1
        mpp[ord(s[right])] -= 1
        while cnt == m:
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                sid = left
            mpp[ord(s[left])] += 1
            if mpp[ord(s[left])] > 0: cnt -= 1
            left += 1
    return s[sid:sid+min_len] if sid != -1 else ""
print("optimal", minimum_window_substring_optimal(s, t))
