'''

We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].
'''
def possibleBipartition(n, dislikes):
    graph=[[] for _ in range(n+1)]
    for u,v in dislikes:
        graph[u].append(v)
        graph[v].append(u)

    color=[-1]*(n+1)
    def bipartit(start,seen, neb):
        seen.add(start)
        color[start]=neb
        for val in graph[start]:
            if val not in seen:
                if not bipartit(val, seen, neb^1):
                    return False
            else:
                if color[start]==color[val]:
                    return False
        return True
    seen=set()
    finalRes=True
    for index in range(1, n+1):
        if index not in seen:
            res=bipartit(index, seen, 0)
            finalRes&=res
    return finalRes

dislikes = [[1,2],[1,3],[2,3]]
n=3
print(possibleBipartition(n, dislikes))