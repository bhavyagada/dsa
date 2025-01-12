arr = [1,1,1,2,2,3,3,3,4,4,5,6,6,6,7]

def remove_duplicates(arr):
    # TC: O(n), SC: O(1)
    k = 0
    for i in range(len(arr)):
        if arr[i] != arr[k]:
            k += 1
            arr[k] = arr[i]
    return arr[:k+1]
print(remove_duplicates(arr))
