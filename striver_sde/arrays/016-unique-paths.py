def unique_paths(n, m):
    N = m + n - 2
    R = n - 1
    res = 1
    for i in range(1, R+1):
        res *= (N - i + 1)
        res //= i
    return res

n = 3
m = 7
res = unique_paths(n, m)
print(res)
assert res == 28