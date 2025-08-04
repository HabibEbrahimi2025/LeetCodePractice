def findOrginalString(word):
    res=1
    i=0
    while i<len(word):
        count=0
        j=i
        while j<len(word)-1 and word[j]==word[j+1]:
            count+=1
            j+=1
        if i==j:
            i+=1
        else:
            i=j
        res+=count
    return res
word = "aabbbbtttt"
print(findOrginalString(word))



        