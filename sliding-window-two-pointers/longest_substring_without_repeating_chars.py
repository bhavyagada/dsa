s = "abcabcbb"

def find_longest_brute(s):
    n = len(s)
    if n == 0: return 0
    max_ans = -1
    for i in range(n):
        st = {}
        for j in range(i, n):
            if s[j] in st:
                max_ans = max(max_ans, j - i)
                break
            st[s[j]] = 1
    return max_ans
print("brute force: ", find_longest_brute(s))

def find_longest_better(s):
    st = set()
    left, max_len = 0, 0
    for right in range(len(s)):
        if s[right] in st:
            while left < right and s[right] in st:
                st.remove(s[left])
                left += 1
        st.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
print("better: ", find_longest_better(s))

def find_longest_optimal(s):
    mpp = [-1] * 256
    left, max_len = 0, 0

    for right in range(len(s)):
        left = max(mpp[ord(s[right])] + 1, left)
        mpp[ord(s[right])] = right
        max_len = max(max_len, right - left + 1)
    return max_len
print("optimal: ", find_longest_optimal(s))
