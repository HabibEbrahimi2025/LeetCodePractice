def checkPolindrom(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

def LongestPolindrom(s):
    finalRes=''
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if checkPolindrom(s[i:j+1]):
                if len(s[i:j+1])>len(finalRes):
                    finalRes=s[i:j+1]
    return finalRes
print(LongestPolindrom("aaaaaaaaaaaaaa"))


