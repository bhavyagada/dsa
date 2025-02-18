bt = [4,3,7,1,2]

def shortest_job_first(bt):
    # optimal => TC: O(n + nlogn), SC: O(1)
    n = len(bt)
    bt.sort()
    time, wait = 0, 0
    for t in bt:
        wait += time
        time += t
    return wait // n
print(shortest_job_first(bt))

