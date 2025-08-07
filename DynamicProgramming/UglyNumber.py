'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

'''
def uglyNumber(n):
    dp=[0]*n
    dp[0]=1
    i2=i3=i5=0
    for i in range(1,n):
        next2=dp[i2]*2
        next3=dp[i3]*3
        next5=dp[i5]*5

        ugly=min(next2, next3, next5)
        dp[i]=ugly
        if ugly==next2:
            i2+=1
        if ugly==next3:
            i3+=1
        if ugly==next5:
            i5+=1
    return dp[-1]
        
        

print(uglyNumber(10))
            

            


