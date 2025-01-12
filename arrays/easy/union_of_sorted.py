arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5]

def union(arr1, arr2):
    # TC: O(m+n), SC: O(m+n) / O(1)
    res = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if not res or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
        else:
            if not res or res[-1] != arr2[j]:
                res.append(arr2[j])
            j += 1

    while i < len(arr1):
        if res[-1] != arr1[i]:
            res.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        if res[-1] != arr2[j]:
            res.append(arr2[j])
        j += 1

    return res
print(union(arr1, arr2))
