'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
'''


from collections import deque
from collections import defaultdict
def findOrder(numCourses, prerequisites):
    graph=defaultdict(list)
    inDegree=[0]*numCourses
    for c,p in prerequisites:
        if not p in graph:
            graph[p]=[c]
        else:
            graph[p].append(c)
        
        inDegree[c]+=1

    que=deque([x for x in range(numCourses) if inDegree[x]==0])

    order=[]
    while que:
        temp=que.popleft()
        order.append(temp)

        for nx in graph[temp]:
            inDegree[nx]-=1
            if inDegree[nx]==0:
                que.append(nx)
    if len(order)!=numCourses:
        return []
    else:
        return order

numCourses = 2
prerequisites = [[1,0]]
print(findOrder(numCourses, prerequisites))