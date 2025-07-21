def fancyString(s):
    if len(s)<2:
        return s
    i=0
    result=[]
    while i<len(s):
        j=1
        if i+1 < len(s) and s[i]==s[i+1]:
            while i+1<len(s) and s[i]==s[i+1]:
                j+=1
                if j<=2:
                    result.append(s[i])
                    i+=1
                else:
                    i+=1
        if i<len(s):           
            result.append(s[i])
            i+=1
    return ''.join(result)


s="leeetcode"
print(fancyString(s))

    

