def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    ans = []
    for start, end in intervals:
        if not ans or start > ans[-1][1]:
            ans.append([start, end])
        else:
            ans[-1][1] = max(end, ans[-1][1])
    return ans

intervals = [[15,18],[2,6],[8,10],[1,3]]
merged = merge_intervals(intervals)
assert merged == [[1,6],[8,10],[15,18]]