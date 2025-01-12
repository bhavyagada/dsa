arr = [3,4,5,1,2]

# is array sorted
def is_sorted(arr):
    # TC: O(n), SC: O(1)
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True
assert is_sorted(arr) == False
print("is array sorted:", is_sorted(arr))

# is array sorted and rotated
def is_sorted_rotated(arr):
    # TC: O(n), SC: O(1)
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[(i+1) % len(arr)]: count += 1
        if count > 1: return False
    return True
assert is_sorted_rotated(arr) == True
print("is array sorted and rotated:", is_sorted_rotated(arr))
