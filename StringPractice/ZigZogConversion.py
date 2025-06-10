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

