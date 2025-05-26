def insertInter(intervals, newInterval):
    addNew=[]
    newPlace=0
    while newPlace<len(intervals) and intervals[newPlace][0]<newInterval[0]:
        addNew.append(intervals[newPlace])
        newPlace+=1
    addNew.append(newInterval)
    for i in range(newPlace, len(intervals)):
        addNew.append(intervals[i])
    
    merge=[]

    for inter in addNew:
        if not merge or merge[-1][1]<inter[0]:
            merge.append(inter)
        else:
            merge[-1][1]=max(merge[-1][1], inter[1])
    return merge

intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]]
print(insertInter(intervals, [4,8]))
