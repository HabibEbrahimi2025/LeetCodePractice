'''
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

'''
from collections import defaultdict
from collections import deque
def minimumHeightTrees(n, edges):
    def levelChecker(start, graph):
        level=0
        que=deque([start])
        seen= set()
        seen.add(start)

        while que:
            n=len(que)
            while n>0:
                temp=que.popleft()
                for nx in graph[temp]:
                    if nx not in seen:
                        seen.add(nx)
                        que.append(nx)
                n-=1
            level+=1
        return level

    graph=defaultdict(list)
    for u,v in edges:
        if u not in graph:
            graph[u]=[v]
        else:
            graph[u].append(v)
        
        if v not in graph:
            graph[v]=[u]
        else:
            graph[v].append(u)
    
    lenght=[0]*n
    minHeight=float('inf')
    for i in range(n):
        res=levelChecker(i, graph)
        minHeight=min(minHeight, res)
        lenght[i]=res

    
    finalRes=[]
    for i, val in enumerate(lenght):
        if val==minHeight:
            finalRes.append(i)
    return finalRes
    
n = 3
edges = [[1,0],[1,2]]
print(minimumHeightTrees(n,edges))

