arr = [[1, 2, 5], [3, 1, 1], [3, 3, 3]]
n = len(arr)

def train_recursion(day, last):
    if day == 0:
        return max(arr[0][i] for i in range(3) if i != last)

    maxi = 0
    for i in range(3):
        if i != last:
            points = arr[day][i] + train_recursion(day-1, i)
            maxi = max(maxi, points)
    return maxi
print("recursion: ", train_recursion(n-1, 3))

def train_memo(day, last, dp):
    if day == 0:
        return max(arr[0][i] for i in range(3) if i != last)

    if dp[day][last] != -1: return dp[day][last]
    maxi = 0
    for i in range(3):
        if i != last:
            points = arr[day][i] + train_memo(day-1, i, dp)
            maxi = max(maxi, points)
    dp[day][last] = maxi
    return dp[day][last]
dp = [[-1 for _ in range(4)] for _ in range(n)]
print("memoization: ", train_memo(n-1, 3, dp))

def train_tab():
    # TC: O(n*4*3), SC: O(n*4)
    dp = [[0 for _ in range(4)] for _ in range(n)]
    dp[0][0] = max(arr[0][1], arr[0][2])
    dp[0][1] = max(arr[0][0], arr[0][2])
    dp[0][2] = max(arr[0][0], arr[0][1])
    dp[0][3] = max(arr[0][0], arr[0][1], arr[0][2])

    for day in range(1, n):
        for last in range(4):
            for task in range(3):
                if task != last: dp[day][last] = max(dp[day][last], arr[day][task] + dp[day-1][task])
    return dp[n-1][3]
print("tabular: ", train_tab())

def train_optimal():
    # TC: O(n*4*3), SC: O(4)
    prev = [0 for _ in range(4)]
    prev[0] = max(arr[0][1], arr[0][2])
    prev[1] = max(arr[0][0], arr[0][2])
    prev[2] = max(arr[0][0], arr[0][1])
    prev[3] = max(arr[0][0], arr[0][1], arr[0][2])

    for day in range(1, n):
        temp = [0 for _ in range(4)]
        for last in range(4):
            for task in range(3):
                if task != last: temp[last] = max(temp[last], arr[day][task] + prev[task])
        prev = temp
    return prev[3]
print("space optimized: ", train_optimal())

