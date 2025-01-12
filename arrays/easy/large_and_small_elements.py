arr = [1,2,3,9,10,10]

# find smallest & second smallest
def find_smallest(arr):
    # TC: O(n), SC: O(1)
    minn, sminn = float('inf'), float('inf')
    for n in arr:
        if n < minn:
            sminn = minn
            minn = n
        if n < sminn and n != minn:
            sminn = n
    return minn, sminn
print("find smallest & second smallest:", find_smallest(arr))

# find largest & second largest
def find_largest(arr):
    # TC: O(n), SC: O(1)
    maxx, smaxx = float('-inf'), float('-inf')
    for n in arr:
        if n > maxx:
            smaxx = maxx
            maxx = n
        if n > smaxx and n != maxx:
            smaxx = n
    return maxx, smaxx
print("find largest & second largest:", find_largest(arr))
