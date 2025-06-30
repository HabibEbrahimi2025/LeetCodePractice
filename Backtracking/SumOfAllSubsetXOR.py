def findXor(path):
    if len(path)==0:
        return 0
    if len(path)==1:
        return path[0]
    
    res=path[0]
    for i in range(1, len(path)):
        res^=path[i]
    return res

def allSubset(start,arr,path, result):
    result[0]+=findXor(path)
    for i in range(start, len(arr)):
        path.append(arr[i])
        allSubset(i+1, arr, path, result)
        path.pop()

result=[0]
allSubset(0,[5,1,6], [], result)
print(result[0])
    