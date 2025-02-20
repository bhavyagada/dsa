s = "aabb"

def partition(ind, n, s, ds, res):
    # TC: O(2^n * n), SC: O(n)
    if ind == n:
        res.append(ds.copy())
        return

    for i in range(ind, n):
        if s[ind:i+1] == s[ind:i+1][::-1]:
            ds.append(s[ind:i+1])
            partition(i+1, n, s, ds, res)
            ds.pop()

res = []
partition(0, len(s), s, [], res)
print(res)

