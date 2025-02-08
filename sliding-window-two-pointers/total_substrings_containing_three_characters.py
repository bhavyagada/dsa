s = "abcabc"

def total_substrings_brute(s):
    # brute => TC: O(n^2), SC: O(1)
    n = len(s)
    cnt = 0
    for i in range(n):
        mpp = [0, 0, 0]
        for j in range(i, n):
            mpp[ord(s[j]) - ord('a')] = 1
            if mpp[0] + mpp[1] + mpp[2] == 3:
                cnt += 1
    return cnt
print("brute", total_substrings_brute(s))

def total_substrings_optimal(s):
    # optimal => TC: O(n), SC: O(1)
    n = len(s)
    cnt = 0
    last_seen = [-1, -1, -1]
    for i in range(n):
        last_seen[ord(s[i]) - ord('a')] = i
        cnt = cnt + (1 + min(last_seen[0], last_seen[1], last_seen[2]))
    return cnt
print("optimal", total_substrings_optimal(s))
