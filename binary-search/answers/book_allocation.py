arr = [25,46,28,49,24]
m = 4

def count(pages, arr):
    n = len(arr)
    students = 1
    student_pages = 0
    for i in range(n):
        if student_pages + arr[i] <= pages:
            student_pages += arr[i]
        else:
            students += 1
            student_pages = arr[i]
    return students

# same as split array largest sum
# same as painters partition
def allocate_books(arr, m):
    # optimal => TC: O(nlog(sum-max)), SC: O(1)
    if m > len(arr): return -1
    low, high = max(arr), sum(arr)
    while low <= high:
        mid = low + (high - low) // 2
        if count(mid, arr) > m:
            low = mid + 1
        else:
            high = mid - 1
    return low
print(allocate_books(arr, m))
