'''

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
'''
from collections import defaultdict
def evaluateDivision(equations, values, queries):
    graph=defaultdict(list)

    for (a,b), val in zip(equations, values):
        graph[a].append((b,val))
        graph[b].append((a,1.0/val))
    

    def dfs(start, end, seen, acc):
        if start==end:
            return acc
        
        seen.add(start)
        for nx, val in graph[start]:
            if nx not in seen:
                result = dfs(nx, end, seen, acc*val)
                if result!=-1:
                    return result
        return -1
    
    res=[]
    for a,b in queries:
        if a not in graph or b not in graph:
            res.append(-1)
        elif a==b:
            res.append(1)
        else:
            res.append(dfs(a,b,set(), 1.0))
    return res


equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

print(evaluateDivision(equations, values, queries))
