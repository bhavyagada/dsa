arr = [1,2,3,4,5,6,7]
k = 3

def rotate_array(arr, k):
    n = len(arr)
    k = k % n # in case k > n
    arr[:] = arr[n-k:] + arr[:n-k] # rotate right
    # or
    arr[:] = arr[k:] + arr[:k] # rotate left
rotate_array(arr, k)
print(arr)
