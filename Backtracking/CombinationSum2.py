def combinationSum2(k,n):
    result=[]

    def backtracking(start, path):
        if len(path)==k:
            if sum(path)==n:
                result.append(path[:])
            return
        
        for i in range(start, len(arr)):
            if arr[i] not in path:
                path.append(arr[i])
                backtracking(arr[i], path)
                path.pop()
    arr=[x for x in range(1,10)]
    backtracking(0,[])
    return result
k=4
n=1
print(combinationSum2(k,n))
