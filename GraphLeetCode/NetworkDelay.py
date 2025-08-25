'''
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
'''
import heapq
def networkDelay(times, n, k):
    graph = {i: [] for i in range(1, n+1)}
    for u, v, w in times:
        graph[u].append((v, w))
    
    heap = [(0, k)]
    cost = {}
    
    while heap:
        t, node = heapq.heappop(heap)
        if node in cost:
            continue
        cost[node] = t
        for nei, w in graph[node]:
            if nei not in cost:
                heapq.heappush(heap, (t + w, nei))
    
    if len(cost) != n:
        return -1
    return max(cost.values())

print(networkDelay([[1,2,1],[2,3,2],[1,3,4]], 3, 1))  # 3
