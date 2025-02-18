start = [0,3,1,5,5,8]
end = [5,4,2,9,7,9]

def maximum_meetings(start, end):
    # optimal => TC: O(nlogn + n), SC: O(1)
    meetings = sorted(zip(start, end), key=lambda x: x[1])
    last_time = meetings[0][1]
    cnt = 1
    for pos in range(1, len(meetings)):
        if meetings[pos][0] > last_time:
            cnt += 1
            last_time = meetings[pos][1]
    return cnt
print(maximum_meetings(start, end))


