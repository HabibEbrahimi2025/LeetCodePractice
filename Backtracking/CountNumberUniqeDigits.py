def countNumberUnique(n):
    if n==0:
        return 1
    if n==1:
        return 10
    
    total=10
    product=9
    avialable=9

    for _ in range(2, n+1):
        product*=avialable
        total+=product
        avialable-=1
    return total

    
print(countNumberUnique(3))

    