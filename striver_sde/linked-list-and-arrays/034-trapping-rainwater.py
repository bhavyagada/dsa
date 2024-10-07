def trap(arr):
    n = len(arr)
    lmax, rmax, total = 0, 0, 0
    l, r = 0, n-1
    while l < r:
        if arr[l] <= arr[r]:
            if lmax > arr[l]:
                total += (lmax - arr[l])
            else:
                lmax = arr[l]
            l += 1
        else:
            if rmax > arr[r]:
                total += (rmax - arr[r])
            else:
                rmax = arr[r]
            r -= 1

    return total

height = [0,1,0,2,1,0,1,3,2,1,2,1]
total = trap(height)
print(total)
assert total == 6
