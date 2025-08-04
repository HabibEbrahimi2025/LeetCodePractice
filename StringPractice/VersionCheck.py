def checkVersion(s1,s2):
    a=s1.split('.')
    b=s2.split('.')
    
    maxRange=max(len(a), len(b))
    for i in range(maxRange):
        first=int(a[i]) if i<len(a[i]) else 0
        second=int(b[i]) if i<len(b[i]) else 0

        if first<second:
            return -1
        if first>second:
            return 1
    return 0

a="1.2"
b="1.10"
print(checkVersion(a,b))
