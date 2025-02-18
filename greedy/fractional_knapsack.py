val = [100,60,100,200]
wt = [20,10,50,50]
capacity = 90

def fractional_knapsack(val, wt, capacity):
    # optimal => TC: O(nlogn + n), SC: O(1) 
    sack = sorted(zip(val, wt), key=lambda x: x[0]/x[1], reverse=True)
    total, W = 0, capacity
    for v, w in sack:
        if w <= W:
            total += v
            W -= w
        else:
            total += ((v / w) * W)
            break
    return total
print(fractional_knapsack(val, wt, capacity))


