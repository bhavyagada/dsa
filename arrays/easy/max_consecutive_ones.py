arr = [1,1,1,0,1,1,1,1]

def max_ones(arr):
    i = 0
    maxx = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            cnt += 1
            maxx = max(maxx, cnt)
        else:
            cnt = 0
    return maxx
print(max_ones(arr))
