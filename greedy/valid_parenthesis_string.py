s = "(*))"

def is_valid_recursion(s, i, cnt):
    # brute => TC: O(3^n), SC: O(n)
    if cnt < 0: return False
    if i == len(s):
        return cnt == 0
    if s[i] == "(":
        return is_valid_recursion(s, i+1, cnt+1)
    if s[i] == ")":
        return is_valid_recursion(s, i+1, cnt-1)
    return is_valid_recursion(s, i+1, cnt+1) or is_valid_recursion(s, i+1, cnt-1) or is_valid_recursion(s, i+1, cnt)
print("brute: ", is_valid_recursion(s, 0, 0))

def is_valid_optimal(s):
    # optimal => TC: O(n), SC: O(1)
    min, max = 0, 0
    for i in range(len(s)):
        if s[i] == "(":
            min += 1
            max += 1
        elif s[i] == ")":
            min -= 1
            max -= 1
        else:
            min -= 1
            max += 1
        if min < 0: min = 0
        if max < 0: return False
    return min == 0
print("optimal: ", is_valid_optimal(s))


