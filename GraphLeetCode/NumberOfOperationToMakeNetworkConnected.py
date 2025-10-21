'''
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
'''
from collections import defaultdict
def numberOperation(n, connections):
    if len(connections)<n-1:
        return -1
    graph=defaultdict(list)
    for u,v in connections:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(start, seen):
        for val in graph[start]:
            if val not in seen:
                seen.add(val)
                dfs(val ,seen)
    totalTree=0
    seen=set()
    for i in range(n):
        if i not in seen:
            seen.add(i)
            dfs(i, seen)
            totalTree+=1
    return totalTree-1

n = 4
connections =  [[0,1],[0,2],[1,2]]
print(numberOperation(n, connections))
