N = 6
r = 5
c = 3

# variation 1
def nCr(n, r):
    # optimal => TC: O(c), SC: O(1)
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res
print("(variation 1) print value at row, column:", nCr(r - 1, c - 1))

def get_row(N):
    # brute force => TC: O(nr), SC: O(1)
    # ans = []
    # for i in range(N):
    #     ans.append(nCr(r - 1, i))
    # return ans

    # optimal => TC: O(n), SC: O(1)
    ans = 1
    res = [1]
    for i in range(1, N):
        ans = ans * (N - i)
        ans = ans // i
        res.append(ans)
    return res
print("(variation 2) print row N:", get_row(N))

def get_triangle(N):
    # optimal => TC: O(n^2), SC: O(1)
    ans = []
    for i in range(1, N + 1):
        ans.append(get_row(i))
    return ans
print("(variation 3) print triangle upto row N:", get_triangle(N))
