def coinChange(coins, amount):
    if amount==0:
        return 0
    result=[0]
    coins.sort(reverse=True)
    def backtracking(currentAmount):
        if currentAmount==0:
            return True
        if currentAmount<0:
            return False
        
        for num in coins:
            result[0]+=1
            if backtracking(currentAmount-num):
                return result[0]
            result[0]-=1
        return -1
    if backtracking(amount)!=-1:
        return result[0]
    else:
        return -1
    
     
coins = [4,5,6,7]
amount = 4
print(coinChange(coins, amount))
