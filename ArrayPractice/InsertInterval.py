'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
'''
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
