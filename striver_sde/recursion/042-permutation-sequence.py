def get_permutation(n, k):
    fact = 1
    numbers = []
    for i in range(1, n):
        fact *= i
        numbers.append(i)
    numbers.append(n)

    ans = ""
    k -= 1
    while True:
        ans += str(numbers[k // fact])
        numbers.pop(k // fact)
        if not numbers: break
        k %= fact
        fact //= len(numbers)
    
    return ans

n = 4
k = 9
ans = get_permutation(n, k)
print(ans)
assert ans == "2314"
