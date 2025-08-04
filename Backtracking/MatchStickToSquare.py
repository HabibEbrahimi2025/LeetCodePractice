'''
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
'''
def matchStickToSquare(matchsticks):
    sumAll=sum(matchsticks)
    if sumAll%4!=0:
        return False
    
    target=sumAll//4
    matchsticks.sort(reverse=True)

    sides=[0]*4

    def backtracking(start):
        if start==len(matchsticks):
            return all(side==target for side in sides)
        for i in range(4):
            if sides[i]+matchsticks[start]<=target:
                sides[i]+=matchsticks[start]
                if backtracking(start+1):
                    return True
                sides[i]-=matchsticks[start]
            if sides[i] == 0:
                break
        return False
    return backtracking(0)
matchsticks = [3,3,3,3,4]
print(matchStickToSquare(matchsticks))
