def maximumNumberEvent(events):
    if len(events)<1:
        return 0
    events.sort(key=lambda x: x[0])

    day=1
    for event in events:
        if day>=event[0] and day<=event[1]:
            day+=1
    return day-1

    
    
events= [[1,2],[1,2], [3,3], [1,5], [1,5]]
print(maximumNumberEvent(events))