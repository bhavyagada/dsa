s = "abcdebdde"
t = "bde"

# output: "bcde"

def backtrack(s, t, right):
    for i in range(len(t) - 1, -1, -1):
        while s[right] != t[i]: right -= 1
    return right

def min_window(s, t):
    # optimal => TC: O(n^2), SC: O(1)
    n, m = len(s), len(t)
    right, tidx, start = 0, 0, -1
    min_len = float('inf')
    while right < n:
        if s[right] == t[tidx]:
            tidx += 1
            if tidx == m:
                left = backtrack(s, t, right)
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                tidx = 0
                right = left
        right += 1
    return "" if start == -1 else s[start:start+min_len]
print(min_window(s, t))
