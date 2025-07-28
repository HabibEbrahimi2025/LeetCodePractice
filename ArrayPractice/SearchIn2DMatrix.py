'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''
def findValue(matrix, target):
    seachRow=0
    while seachRow<len(matrix)-1 and target>matrix[seachRow][-1]:
        seachRow+=1
    
    for val in matrix[seachRow]:
        if target==val:
            return True
    return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(findValue(matrix, 10))