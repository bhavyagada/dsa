g = [1,2,3]
s = [1,2]

def assign_cookies(g, s):
    # optimal => O(nlogn + mlogn + n + m), SC: (1)
    g.sort()
    s.sort()
    n, m = len(g), len(s)
    left, right = 0, 0
    while left < n and right < m:
        if g[left] <= s[right]:
            left += 1
        right += 1
    return left
print(assign_cookies(g, s))
