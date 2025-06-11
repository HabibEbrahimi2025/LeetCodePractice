def checkValidP(pranth):
    stack=[]
    for p in pranth:
        if p=='(':
            stack.append(p)
        elif p==')' and stack:
            stack.pop()
        else:
            return False
    if stack:
        return False
    else:
        return True
#print(checkValidP("((()))"))

def generatePranthesis(n):
    if n==0:
        return []
    if n==1:
        return ["()"]
    
    def backtracking(current, openCount, closeCount, result):
        if len(current)==2*n:
            result.append(current)
            return
        if openCount<n:
            backtracking(current+"(", openCount+1, closeCount, result)
        if closeCount<openCount:
            backtracking(current+")", openCount, closeCount+1, result)
    result=[]
    backtracking("", 0, 0, result)
    return result
print(generatePranthesis(8))




