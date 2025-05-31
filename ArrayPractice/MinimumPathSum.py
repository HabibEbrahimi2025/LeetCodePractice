def minimumPathSum(grid):
    def check(grid, checker, i, j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
            return False
        if checker[i][j]:
            return False
        return True

    def findPathSum(grid, i,j, path, checker):
        if i==len(grid)-1 and j==len(grid[0])-1:
            sumVal=sum(path[1])
            if sumVal<path[0]:
                path[0]=sumVal
            return
        for x,y in ((0,1),(1,0)):
            n,m=i+x, j+y
            if check(grid, checker, n,m):
                path[1].append(grid[n][m])
                checker[n][m]=True
                findPathSum(grid, n,m,path,checker)
                path[1].pop()
                checker[n][m]=False
    checker=[[False] * len(grid[0]) for _ in range(len(grid))]
    path=[float('inf'), []]
    path[1].append(grid[0][0])
    checker[0][0]=True
    findPathSum(grid,0,0,path, checker)
    return path[0]

grid = [[1,2],[1,2]]
print(minimumPathSum(grid))         