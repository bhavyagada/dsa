arr = [9,6,4,2,3,5,8,0,1]

def missing_number(arr):
    # TC: O(n), SC: O(1)
    n = len(arr)
    s1 = n * (n + 1) // 2
    s2 = 0
    for i in arr: s2 += i
    return s1 - s2
print(missing_number(arr))
