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
