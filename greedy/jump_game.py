arr = [1,2,4,1,1,0,2,5]

def jump_game(arr):
    # optimal => TC: O(n), SC: O(1)
    n = len(arr)
    maxId = 0
    for i in range(n):
        if i > maxId: return False
        maxId = max(maxId, i + arr[i])
    return True
print(jump_game(arr))

