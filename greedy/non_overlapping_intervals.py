intervals = [[1,2],[2,3],[3,4],[1,3]]

def non_overlapping(intervals):
    intervals = sorted(intervals, key=lambda x: x[1])
    last_time = intervals[0][1]
    cnt = 1
    for pos in range(1, len(intervals)):
        if intervals[pos][0] >= last_time:
            cnt += 1
            last_time = intervals[pos][1]
    return len(intervals) - cnt
print(non_overlapping(intervals))

