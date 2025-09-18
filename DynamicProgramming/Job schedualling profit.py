'''
Job schedualling with profit 
'''
def eventOrganizer(arr):
    allHour=[[0]*(49) for _ in range(49)]

    for st, ed, cost in arr:
        allHour[st][ed]=max(allHour[st][ed], cost)

    costAllHour=[0]*49

    for i in range(49):
        for j in range(i):
            costAllHour[i]=max(costAllHour[i], allHour[j][i]+costAllHour[j])
    print(costAllHour[48])


t=int(input())
for _ in range(t):
    n=int(input())
    arr=[]
    for _ in range(n):
        a,b,c=list(map(int, input().split()))
        arr.append((a,b,c))
    eventOrganizer(arr)

#arr=[(1,2,100),(2,3,200),(3,4,1600),(1,3,2100)]
#eventOrganizer(arr)
