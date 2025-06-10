def LongestSubSringWithoutRepeatC(s):
    ss=set()
    finalLenth=0
    i=0
    for j in range(len(s)):
        while s[j] in ss:
            ss.remove(s[i])
            i+=1
        ss.add(s[j])
        if (n:=j-i+1)>finalLenth:
            finalLenth=n
    return finalLenth
print(LongestSubSringWithoutRepeatC("bbbbb"))