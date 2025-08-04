'''

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
'''
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

