def grayCode(n):
    arr=[]
    for i in range(2**n):
        res=bin(i)
        arr.append(res[2:].zfill(n))
    print(arr)

def grayCode2(n):
    arr=[]
    for i in range(2**n):
        arr.append(i^(i>>1))
    print(arr)
grayCode2(4)