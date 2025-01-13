arr = [10,22,12,3,0,6]

def find_leaders(arr):
    # optimal => TC: O(n), SC: O(n)
    res = []
    last_lead = float('-inf')
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > last_lead:
            last_lead = arr[i]
            res.append(arr[i])
        else:
            continue
    return res[::-1]
print(find_leaders(arr))
