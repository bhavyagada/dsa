# print name N times
def print_name(i, n):
    # TC: O(n), SC: O(n)
    if i > n: return # base case
    print("Bhavya")
    print_name(i + 1, n) # recursion call
print("\nprint name N times:")
print_name(1, 5)

# print 1 to N
def print_1_to_n(i, n):
    # TC: O(n), SC: O(n)
    if i > n: return
    print(i)
    print_1_to_n(i + 1, n)
print("\nprint 1 to N:")
print_1_to_n(1, 5)

# print 1 to N (using backtracking)
def print_1_to_n_backtrack(i, n):
    # TC: O(n), SC: O(n)
    if i < 1: return
    print_1_to_n_backtrack(i - 1, n)
    print(i)
print("\nprint 1 to N (using backtracking):")
print_1_to_n_backtrack(5, 5)

# print N to 1
def print_n_to_1(i, n):
    # TC: O(n), SC: O(n)
    if i < 1: return
    print(i)
    print_n_to_1(i - 1, n)
print("\nprint N to 1:")
print_n_to_1(5, 5)

# print N to 1 (using backtracking)
def print_n_to_1_backtrack(i, n):
    # TC: O(n), SC: O(n)
    if i > n: return
    print_n_to_1_backtrack(i + 1, n)
    print(i)
print("\nprint N to 1 (using backtracking):")
print_n_to_1_backtrack(1, 5)

# sum of first N numbers (parameterized)
def sum_of_first_N(i, n, total):
    # TC: O(n), SC: O(n)
    if i > n:
        print(total)
        return
    sum_of_first_N(i + 1, n, total + i)
print("\nsum of first N numbers (parameterized):")
sum_of_first_N(1, 5, 0)

# sum of first N numbers (functional)
def sum_of_first_N(n):
    # TC: O(n), SC: O(n)
    if n == 0: return 0
    return n + sum_of_first_N(n - 1)
print("\nsum of first N numbers (functional):")
print(sum_of_first_N(5))

# factorial of a number
def factorial(n):
    # TC: O(n), SC: O(n)
    if n == 1: return 1
    return n * factorial(n - 1)
print("\nfactorial of a number:")
print(factorial(5))

# reverse an array
def reverse(arr, i, n):
    # TC: O(n), SC: O(1)
    if i >= n: return
    arr[i], arr[n] = arr[n], arr[i]
    reverse(arr, i + 1, n - 1)
print("\nreverse an array:")
arr = [1,2,3,4,5]
reverse(arr, 0, len(arr) - 1)
print(arr)

# check if string is palindrome
def check_palindrome(str, i, n):
    # TC: O(n), SC: O(n)
    if i >= n: return True
    if str[i] != str[n]: return False
    return check_palindrome(str, i + 1, n - 1)
print("\ncheck if string is palindrome:")
str = "madam"
print(check_palindrome(str, 0, len(str) - 1))

# print fibonacci series up to Nth term
def fibonacci(n):
    # TC: O(2^n), SC: O(n)
    if n <= 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print("\nfibonacci number:")
print(fibonacci(8))
