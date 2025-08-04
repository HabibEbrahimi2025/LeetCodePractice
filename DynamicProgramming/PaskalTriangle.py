'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

'''

def paskalTriangle(numRows):
    def generateLevel(k):
        arr=[[1]*k for _ in range(k)]

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if i==0 or j==0 or i==j:
                    continue
                else:
                    arr[i][j]=arr[i-1][j]+arr[i-1][j-1]
        return arr[k-1]
    
    res=[]
    for i in range(1, numRows+1):
        res.append(generateLevel(i))
    return res
print(paskalTriangle(12))