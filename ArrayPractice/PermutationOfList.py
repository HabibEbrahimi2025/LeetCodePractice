def permut(arr):
    res=[]

    def backtrack(start):
        if start==len(arr):
            res.append(arr[:])
            return
        for i in range(start, len(arr)):
            arr[start], arr[i]=arr[i], arr[start]
            backtrack(start+1)
            arr[start],arr[i]=arr[i],arr[start]
    backtrack(0)
    print(res)
permut([1,2,3,4])