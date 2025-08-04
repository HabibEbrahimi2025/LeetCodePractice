def findUniqePath(obstacleGrid):
    def checkState(arr, i,j):
        if i<0 or i>=len(arr) or j<0 or j>=len(arr[0]):
            return False
        if arr[i][j]==1:
            return False
        return True
    
    def findPath(x1,y1,obstacleGrid, move,path):
        if x1==y1 and x1==len(obstacleGrid)-1:
            path[0]+=1
            return
        
        for mm in move:
            if checkState(obstacleGrid,x1+mm[0], y1+mm[1]):
                obstacleGrid[x1+mm[0]][y1+mm[1]]=1
                findPath(x1+mm[0], y1+mm[1], obstacleGrid, move, path)
                obstacleGrid[x1+mm[0]][y1+mm[1]]=0
    move=((0,1),(1,0))
    path=[0]
    findPath(0,0, obstacleGrid, move, path)
    return path[0]
obstacleGrid = [[1]]
print(findUniqePath(obstacleGrid))
        

