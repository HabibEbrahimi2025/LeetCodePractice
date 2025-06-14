def decoder(ss):
    n=len(ss)

    if n==0 or ss[0]=='0':
        return 0
    
    dp=[0]*(n+1)

    dp[0]=1
    dp[1]=1
    for i in range(2, n+1):
        if ss[i-1]!='0':
            dp[i]+=dp[i-1]
        
        towNumber=int(ss[i-2:i])
        if 10<=towNumber<=26:
            dp[i]+=dp[i-2]
    return dp[n]

ss="122123"
print(decoder(ss))
