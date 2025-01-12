arr = [0,1,0,3,12]

def move_zeroes(arr):
    # TC: O(n), SC: O(1)
    idx = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            idx = i
            break
    
    if idx != -1:
        for i in range(idx + 1, len(arr)):
            if arr[i] != 0:
                arr[i], arr[idx] = arr[idx], arr[i]
                idx += 1
move_zeroes(arr)
print(arr)
