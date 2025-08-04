def sodukuBasic(arr):
    allPath=((0,-1),(0,1), (-1,0),(1,0))
    allIndex = [False]*10

    def checkFill(arrCheck):
        for i in range(len(arrCheck)):
            for j in range(len(arrCheck[0])):
                if arrCheck[i][j]==0:
                    return False
        return True
    
    def checkTraverse(n,m, see):
        if (n<0 or n>=len(see)) or (m<0 or m>=len(see[0])):
            return False
        if see[n][m]:
            return False
        return True
    

    def backtracking(x,y, seen):

        if arr[x][y] ==0:
            num=0
            for i in range(1, len(allIndex)):
                if not allIndex[i]:
                    num=i
                    allIndex[i]=True
                    break
            arr[x][y]=num
            seen[x][y]=True
        else:
            allIndex[arr[x][y]]=True

        if x==len(arr)-1 and y==len(arr[0])-1:
            if checkFill(arr):
                return True
            return False
        

        for a,b in allPath:
            aa=a+x
            bb=b+y
            if checkTraverse(aa,bb, seen):
                if backtracking(aa,bb,seen):
                    return True
        return False
    
    seen=[[False]*len(arr) for _ in range(len(arr))]
    print(backtracking(0,0,seen))
    print(arr)

arr=[
    [0,0,2],
    [0,3,0],
    [7,0,0]
]

sodukuBasic(arr)

            