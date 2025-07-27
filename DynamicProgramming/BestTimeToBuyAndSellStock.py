def bestTimeToBuyAndSell(prices):
    res=0
    for i in range(len(prices)):
        buy=prices[i]
        for j in range(i+1, len(prices)):
            sell =prices[j]
            if (n:=sell-buy)>res:
                res=n
    return res
prices = [2,1,2,0,1]
#print(bestTimeToBuyAndSell(prices))


def bestTime(prices):
    buy=float('inf')
    sell=0

    for i in range(len(prices)):
        if prices[i]<buy:
            buy=prices[i]
        currentProfit= prices[i]-buy
        if currentProfit>sell:
            sell=currentProfit

    return sell

print(bestTime(prices))

