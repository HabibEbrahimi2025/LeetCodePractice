def divisorGame(n):
    arr=[False] * (n+1)

    for i in range(2, n+1):
        for x in range(1, i):
            if i%x==0 and not arr[i-x]:
                arr[i]=True
                break
    return arr[n]
print(divisorGame(1))
