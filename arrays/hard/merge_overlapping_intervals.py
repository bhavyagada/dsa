intervals = [[1,3],[2,6],[8,10],[15,18]]

def merge_intervals(intervals):
    # optimal => TC: O(nlogn) + O(n), SC: O(n)
    intervals.sort()
    res = []
    for i in range(len(intervals)):
        if not res or intervals[i][0] > res[-1][1]:
            res.append(intervals[i])
        else:
            res[-1][1] = max(res[-1][1], intervals[i][1])
    return res
print(merge_intervals(intervals))
