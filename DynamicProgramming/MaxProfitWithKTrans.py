def maxProfitWithK(prices, k):
    trans=[[0]*len(prices) for _ in range(k+1)]
    
    for i in range(1,len(trans)):
        for j in range(1, len(trans[0])):
            maxVal=0
            for m in range(j):
                maxVal=max(maxVal, prices[j]-prices[m]+trans[i-1][m])
            trans[i][j]=max(trans[i][j-1], maxVal)
    return trans[k][len(prices)-1]
k=1
prices=[5,11,3,50,60,90]
print(maxProfitWithK(prices, k))