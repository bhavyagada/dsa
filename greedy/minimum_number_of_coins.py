coins = [1,2,5,10,20,50,100,500,1000]
sum = 89

def min_coins(coins, sum):
    # optimal => TC: O(sum), SC: O(1)
    total, cap = 0, sum
    for i in range(len(coins) - 1, -1, -1):
        if coins[i] > cap: continue
        else:
            total += (cap // coins[i])
            cap -= (cap // coins[i]) * coins[i]
    return total
print(min_coins(coins, sum))

