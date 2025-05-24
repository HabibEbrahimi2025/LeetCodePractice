def merge(intervals):
    merge=[]

    intervals.sort(key=lambda x:x[0])

    for inter in intervals:
        if not merge or merge[-1][1]<inter[0]:
            merge.append(inter)
        else:
            merge[-1][1]=max(merge[-1][1], inter[1])
    return merge

intervals =[[1,4],[4,5]]
print(merge(intervals))