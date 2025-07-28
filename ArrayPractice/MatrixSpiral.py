'''
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
'''

def check(seen, arr,  i,j):
    if seen[i][j]:
        return False
    if i<0 or i>len(arr)-1 or j<0 or j>len(arr[0])-1:
        return False
    
    return True

def matrixDisplay(matrix):
    result=[]
    if not matrix:
        return result
    
    top, bottom=0, len(matrix)-1
    left, right=0, len(matrix[0])-1

    while top<=bottom and left<=right:
        for col in range(left, right+1):
            result.append(matrix[top][col])
        top+=1

        for row in range(top, bottom+1):
            result.append(matrix[row][right])
        right-=1

        if top<=bottom:
            for col in range(right, left-1, -1):
                result.append(matrix[bottom][col])
            bottom-=1
        if left<=right:
            for row in range(bottom, top-1, -1):
                result.append(matrix[row][left])
            left+=1
    return result
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(matrixDisplay(matrix))
    