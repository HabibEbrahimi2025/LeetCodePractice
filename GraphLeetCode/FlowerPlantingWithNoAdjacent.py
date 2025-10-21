'''
You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. In each garden, you want to plant one of 4 types of flowers.

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

 

Example 1:

Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
'''
from collections import defaultdict
def gardingNFlower(n, paths):
    graph=defaultdict(list)
    for u, v in paths:
        graph[u].append(v)
        graph[v].append(u)
    res=[0]*(n+1)
    for i in range(1,n+1):
        nebColor=[]
        for val in graph[i]:
            if res[val]!=0:
                nebColor.append(res[val])
        
        for color in range(1, 5):
            if color not in nebColor:
                res[i]=color
                break
    return res[1:]

n = 4
paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
print(gardingNFlower(n, paths))
