from collections import defaultdict
def minPathToConnectAll(graphlist):
    graph=defaultdict(list)
    inDegree=defaultdict(lambda:0)
    for u,v in graphlist:
        graph[u].append(v)
        inDegree[v]+=1
    for x, y in graphlist:
        if x not in inDegree:
            inDegree[x]=0
    total=0
    for key, value in inDegree.items():
        if value==0:
            total+=1
    return total

graphlist=[['Kabul', 'Ghazni'],['Ghazni', 'Zabul'],['Qandahar', 'Helmand'],
           ['Helmand', 'Farah'], ['Daikundi', 'Ghor'],['Ghor', 'Herat']]

print(minPathToConnectAll(graphlist))
