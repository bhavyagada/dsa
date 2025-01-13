prices = [7,1,5,3,6,4]

def max_profit(prices):
    # optimal => TC: O(n), SC: O(1)
    max_profit, min_buy_price = 0, float('inf')
    for i in range(len(prices)):
        min_buy_price = min(min_buy_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_buy_price)
    return max_profit
print(max_profit(prices))
