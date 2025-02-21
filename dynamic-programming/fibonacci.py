n = 10

# recursion
def fib_recursion(n):
    # TC: O(2^n), SC: O(n)
    if n <= 1: return n
    return fib_recursion(n-1) + fib_recursion(n-2)
print("recursion: ", fib_recursion(n))

# memoization
dp = [-1] * (n+1)
def fib_memo(n, dp):
    # TC: O(n), SC: O(n) + O(n)
    if n <= 1: return n
    if dp[n] != -1: return dp[n]
    dp[n] = fib_memo(n-1, dp) + fib_memo(n-2, dp)
    return dp[n]
print("memoization: ", fib_memo(n, dp))

# tabulation
dp = [-1] * (n+1)
def fib_tab(n, dp):
    # TC: O(n), SC: O(n)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print("tabulation: ", fib_tab(n, dp))

# space optimization
def fib(n):
    # TC: O(n), SC: O(1)
    fib0, fib1 = 0, 1
    for _ in range(2, n+1):
        curr = fib0 + fib1
        fib0 = fib1
        fib1 = curr
    return fib1
print("space optimized: ", fib(n))


