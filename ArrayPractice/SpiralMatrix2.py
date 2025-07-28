'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
'''
def spiral2(n):
    spiralMatrix=[[0 for _ in range(n)] for _ in range(n)]

    left, right=0, n-1
    top, bottom=0, n-1
    count=1
    while top<=bottom and left <=right:
        for col in range(left, right+1):
            spiralMatrix[top][col]=count
            count+=1
        top+=1

        for row in range(top, bottom+1):
            spiralMatrix[row][right]=count
            count+=1
        right-=1

        if top<=bottom:
            for col in range(right, left-1, -1):
                spiralMatrix[bottom][col]=count
                count+=1
            bottom-=1
        if left<=right:
            for row in range(bottom, top-1, -1):
                spiralMatrix[row][left]=count
                count+=1
            left+=1
    return spiralMatrix

print(spiral2(2))
