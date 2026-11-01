def stocks(prices):
    n=len(prices)
    min_price=prices[0]
    max_profit=0
    for i in range(1,n):
        if prices[i]<min_price:
            min_price=prices[i]
        profit=prices[i]-min_price
        if profit > max_profit:
            max_profit=profit
    return max_profit
prices=[9,7,3,6,1,7,9,100]
print(stocks(prices))
#time complexity - o(n)
# space complexity - o(1)
