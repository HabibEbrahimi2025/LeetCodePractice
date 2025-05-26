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