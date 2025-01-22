weights = [5,4,5,2,3,4,5,6]
d = 10

def num_of_days(cap, weights):
    n = len(weights)
    days = 1
    load = 0
    for i in range(n):
        if load + weights[i] > cap:
            load = weights[i]
            days += 1
        else:
            load += weights[i]
    return days

def find_capacity(weights, d):
    # optimal => TC: O(nlog(sum-max)), SC: O(1)
    low, high = max(weights), sum(weights)    
    while low <= high:
        mid = low + (high - low) // 2
        if num_of_days(mid, weights) <= d:
            high = mid - 1
        else:
            low = mid + 1
    return low
print(find_capacity(weights, d))
