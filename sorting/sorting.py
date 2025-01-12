# selection sort
def selection_sort(arr):
    # TC: O(n^2), SC: O(1)
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]: mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
selection_arr = [12,3,10,6,15,9,11,8,0,13]
selection_sort(selection_arr)
print("selection sort:", selection_arr)

# bubble sort
def bubble_sort(arr):
    # TC: O(n^2), SC: O(1)
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
bubble_arr = [12,3,10,6,15,9,11,8,0,13]
bubble_sort(bubble_arr)
print("bubble sort:", bubble_arr)

# bubble sort (recursion)
def bubble_sort(arr, i, n):
    # TC: O(n^2), SC: O(n)
    if i == n: return
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
    bubble_sort(arr, i + 1, n)
bubble_arr = [12,3,10,6,15,9,11,8,0,13]
bubble_sort(bubble_arr, 0, len(bubble_arr))
print("bubble sort (recursion):", bubble_arr)

# insertion sort
def insertion_sort(arr):
    # TC: O(n^2), SC: O(1)
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
insertion_arr = [12,3,10,6,15,9,11,8,0,13]
insertion_sort(insertion_arr)
print("insertion sort:", insertion_arr)

# insertion sort (recursion)
def insertion_sort(arr, i, n):
    # TC: O(n^2), SC: O(n)
    if i == n: return
    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1
    insertion_sort(arr, i + 1, n)
insertion_arr = [12,3,10,6,15,9,11,8,0,13]
insertion_sort(insertion_arr, 0, len(insertion_arr))
print("insertion sort (recursion):", insertion_arr)

# merge sort
def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1): 
        arr[i] = temp[i - low]

def merge_sort(arr, low, high):
    # TC: O(nlogn), SC: O(n)
    if low >= high: return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)
merge_arr = [12,3,10,6,15,9,11,8,0,13]
merge_sort(merge_arr, 0, len(merge_arr) - 1)
print("merge sort:", merge_arr)

# quick sort
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1

        while arr[j] > pivot and j >= low + 1:
            j -= 1

        if i < j: 
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    # TC: O(nlogn), SC: O(1)
    if low < high:
        pidx = partition(arr, low, high)
        quick_sort(arr, low, pidx - 1)
        quick_sort(arr, pidx + 1, high)
quick_arr = [12,3,10,6,15,9,11,8,0,13]
quick_sort(quick_arr, 0, len(quick_arr) - 1)
print("quick sort:", quick_arr)
