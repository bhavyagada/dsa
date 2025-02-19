# print name n times
def print_name(name, n):
    if n == 0: return
    print(name)
    print_name(name, n - 1)
print("print name N times")
print_name("Bhavya", 3)
print()

arr = [5,4,3,2,1]
def reverse_arr(arr, n, i):
    if i >= n // 2: return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    reverse_arr(arr, n, i + 1)
print("reverse an array")
reverse_arr(arr, len(arr), 0)
print(arr)
print()

s = "madam"
def is_palindrome(s, n, i):
    if i >= n // 2: return True
    if s[i] != s[n - i - 1]: return False
    return is_palindrome(s, n, i + 1)
print("is string palindrome")
print(is_palindrome(s, len(s), 0))
print()

# print Nth fibonacci number
def fib(n):
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)
print("print Nth fibonacci number")
print(fib(10))
print()

