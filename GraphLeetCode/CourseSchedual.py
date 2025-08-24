'''

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

'''

from collections import defaultdict
from collections import deque
def courseSchedual(numCourses, prerequisites):
    graph=defaultdict(list)
    for c,p in prerequisites:
        if not graph[p]:
            graph[p]=[c]
        else:
            graph[p].append(c)
    
    
    inDegree=[0]*numCourses
    for i in range(numCourses):
        for val in graph[i]:
            inDegree[val]+=1
    que=deque([x for x in range(numCourses) if inDegree[x]==0])
    visited=0
    while que:
        temp=que.popleft()
        visited+=1
        for nx in graph[temp]:
            inDegree[nx]-=1
            if inDegree[nx]==0:
                que.append(nx)
    return visited==numCourses




    

    print(inDegree)
    
    # def cycleDetect(start, graph,parent, seen):
        
    #     for nx in graph[start]:
    #         if nx not in seen:
    #             seen.add(nx)
    #             cycleDetect(nx, graph, start, seen)
    #         elif nx!=parent:
    #             check[0]=False
    # seen=set()
    # seen.add(0)
    # check=[True]

    # cycleDetect(0, graph, -1,seen)
    # if check[0]:
    #     if len(seen)==numCourses:
    #         return True
    #     else:
    #         return False
    # else:
    #     return False
    


prerequesties=[[1,0],[0,1]]
print(courseSchedual(2,prerequesties))

