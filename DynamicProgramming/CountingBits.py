def countingBits(n):
    arr=[0]*(n+1)
    arr[1]=1

    for i in range(2, n+1):
        arr[i]=arr[i>>1]+(i&1)
    return arr
print(countingBits(5))
