def loudAndRich(richer, quiet):
    n=len(quiet)
    reverseGraph=[[] for _ in range(n)]
    for u,v in richer:
        reverseGraph[v].append(u)

    def dfs(start, graph):
        if quiet[start]<result[0]:
            result[0]=quiet[start]
        for neb in graph[start]:
            dfs(neb, graph)

    finalRes=[0]*(n)
    for i in range(n):
        result=[float('inf')]
        dfs(i,reverseGraph)
        finalRes[i]=result[0]
    returnable=[0]*(n)
    for i in range(n):
        returnable[i]=quiet.index(finalRes[i])
    return returnable


richer = []
quiet = [1,0]

print(loudAndRich(richer, quiet))