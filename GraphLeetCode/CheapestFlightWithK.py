def cheapestFlight(n, flights, src, dst, k):
    graph=[[0]*n for _ in range(n)]

    for val in flights:
        graph[val[0]][val[1]]=val[2]
    finalRes=[float('inf')]
    seen=[False]*n
    
    def backtracking(sr,dist,k, path=[]):
        if sr==dist:
            if sum(path)<finalRes[0]:
                finalRes[0]=sum(path)
            return
        if k<0:
            return
        for i in range(len(graph)):
            if graph[sr][i]!=0 and not seen[i]:
                path.append(graph[sr][i])
                seen[i]=True
                backtracking(i, dist, k-1, path)
                path.pop()
                seen[i]=False
    seen[src]=True
    backtracking(src, dst, k)
    if finalRes[0]==float('inf'):
        return -1
    else:
        return finalRes[0]
flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
src = 2
dst = 1
k = 1
n=5
print(cheapestFlight(n, flights, src, dst, k))

