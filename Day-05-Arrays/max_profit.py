def maximum_profit(prices):
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
            
        else:
            profit = price - min_price
            
        if profit > max_profit:
            max_profit = profit
    return max_profit

print(maximum_profit([7,1,5,3,6,4]))