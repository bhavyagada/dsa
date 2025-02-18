intervals = [[1,3],[6,9]]
newInterval = [2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

def insert_intervals(intervals, newInterval):
    # optimal => TC: O(n), SC: O(n)
    n = len(intervals)
    res = []
    i = 0
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)

    while i < n:
        res.append(intervals[i])
        i += 1
    return res
print(insert_intervals(intervals, newInterval))

