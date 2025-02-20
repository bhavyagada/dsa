n = 4
k = 17

# brute force => use recursion to generate all permutations, sort the list and get kth permutation
# TC: O(n! * n) + O(n!logn!), SC: O(n!)

def permutation_sequence(n, k):
    # optimal => TC: O(n^2), SC: O(n)
    fact = 1
    numbers = []
    for i in range(1, n):
        fact = fact * i
        numbers.append(i)
    numbers.append(n)
    ans = ""
    k = k - 1
    while True:
        ans = ans + str(numbers[k//fact])
        numbers.remove(numbers[k//fact])
        if len(numbers) == 0: break
        k = k % fact
        fact = fact // len(numbers)
    return ans
print(permutation_sequence(n, k))

