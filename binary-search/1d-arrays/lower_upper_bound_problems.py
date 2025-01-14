arr = [3,5,8,15,19,19,19,22]
x = 19

# ceil of x (return element instead of its index)
# search insert position
# lower bound
def lower_bound(arr, x):
    # optimal => TC: O(logn), SC: O(1)
    low, high = 0, len(arr) - 1
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
print("lower bound:", lower_bound(arr, x))
print("insert position of x is same as its lower bound!")
print("ceil of x is the element at the lower bound of x!")

def upper_bound(arr, x):
    # optimal => TC: O(logn), SC: O(1)
    low, high = 0, len(arr) - 1
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
print("upper bound:",upper_bound(arr, x))

# ceil is same as lower bound
def floor(arr, x):
    # optimal => TC: O(logn), SC: O(1)
    low, high = 0, len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            ans = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    return ans
print("floor of x:", floor(arr, x))

# lower bound + upper bound
def first_last_occurence(arr, x):
    # optimal => TC: O(2logn), SC: O(1)
    lb = lower_bound(arr, x)
    if lb == len(arr) or arr[lb] != x: return [-1, -1]
    return [lb, upper_bound(arr, x) - 1]
print("first and last occurences of x:", first_last_occurence(arr, x))

# lower bound + upper bound
def count_occurences(arr, x):
    # optimal => TC: O(2logn), SC: O(1)
    lb = lower_bound(arr, x)
    ub = upper_bound(arr, x)
    if lb == len(arr) or arr[lb] != x: return 0
    return ub - lb
print("count occurences of x:", count_occurences(arr, x))
