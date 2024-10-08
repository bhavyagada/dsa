def generate_palindrome_partitions(idx, s, n, ds, ans):
    if idx == n:
        ans.append(ds.copy())
        return
    
    for i in range(idx, n):
        if s[idx:i+1] == s[idx:i+1][::-1]:
            ds.append(s[idx:i+1])
            generate_palindrome_partitions(i+1, s, n, ds, ans)
            ds.pop()

s = "aab"
n = len(s)
ans = []
generate_palindrome_partitions(0, s, n, [], ans)
print(ans)
assert ans == [["a","a","b"],["aa","b"]]
