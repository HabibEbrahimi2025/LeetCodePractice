'''

You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]

'''
from collections import deque, defaultdict
def shortestAlternatingPaths(n, redEdges, blueEdges):
    red_adj = defaultdict(list)
    blue_adj = defaultdict(list)
    
    for a, b in redEdges:
        red_adj[a].append(b)
    for u, v in blueEdges:
        blue_adj[u].append(v)
    queue = deque([(0, "red", 0), (0, "blue", 0)]) 
    visited = set([(0, "red"), (0, "blue")])
    res = [-1] * n
    res[0] = 0
    while queue:
        node, color, dist = queue.popleft()
        if color == "red":
            next_adj = blue_adj
            next_color = "blue"
        else:
            next_adj = red_adj
            next_color = "red"
        for nei in next_adj[node]:
            if (nei, next_color) not in visited:
                visited.add((nei, next_color))
                queue.append((nei, next_color, dist + 1))
                if res[nei] == -1:
                    res[nei] = dist + 1
    return res
redEdges = [[0,1],[1,2]]
blueEdges = []
n = 3
print(shortestAlternatingPaths(n, redEdges, blueEdges))