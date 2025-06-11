def countAndSay(s):
    i=0
    res=''
    while i<len(s):
        count=1
        while i+1< len(s) and s[i]==s[i+1]:
            count+=1
            i+=1
        res+=str(count)
        res+=s[i]
        i+=1
    return res

s="1"
for i in range(3):
    s=countAndSay(s)
print(s)


