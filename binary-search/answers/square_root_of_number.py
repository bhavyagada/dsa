n = 28

def square_root(n):
    # brute force => TC: O(n), SC: (1)
    # ans = 1
    # for i in range(1, n+1):
    #     if i * i <= n:
    #         ans = i
    #     else:
    #         break
    # return ans

    # optimal => TC: O(logn), SC: O(1)
    low, high = 1, n
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            low = mid + 1
        else:
            high = mid - 1
    return high
print(square_root(n))
