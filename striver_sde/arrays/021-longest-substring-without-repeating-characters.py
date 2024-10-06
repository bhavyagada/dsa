def length_of_longest_substring(s):
    n = len(s)
    if n == 0: return 0
    maxans = float('-inf')
    setx = set()
    left = 0
    for right in range(n):
        if s[right] in setx:
            while left < right and s[left] in setx:
                setx.remove(s[left])
                left += 1
        setx.add(s[right])
        maxans = max(maxans, right - left + 1)
    return maxans

s = "abcabcbb"
ans = length_of_longest_substring(s)
print(ans)
assert ans == 3
