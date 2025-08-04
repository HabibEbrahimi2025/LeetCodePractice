'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
'''
def zigZogConversion(s, row):
    if row<=1:
        return s
    arr=[[] for _ in range(row)]

    countRow=0
    asc=True
    for ch in s:
        if countRow==row-1:
            asc=False
        if countRow==0:
            asc=True

        if asc:
            arr[countRow].append(ch)
            countRow+=1
        else:
            arr[countRow].append(ch)
            countRow-=1
    res=''
    for i in range(row):
        for j in range(len(arr[i])):
            res+=''.join(arr[i][j])
    return res

s = "ab"
row=1
print(zigZogConversion(s, row))

