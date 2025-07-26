def paskalTriangle(rowIndex):
    def generateLevel(k):
        arr=[[1]*k for _ in range(k)]

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if i==0 or j==0 or i==j:
                    continue
                else:
                    arr[i][j]=arr[i-1][j]+arr[i-1][j-1]
        return arr[k-1]
    
    res=generateLevel(rowIndex+1)
    return res
print(paskalTriangle(3))