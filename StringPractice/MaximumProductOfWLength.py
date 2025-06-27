def maxiMumPWL(words):
    if len(words)<=1:
        return 0
    
    def checkPair(a,b):
        for ch in b:
            if ch in a:
                return False
        return True
    
    result=0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if checkPair(words[i], words[j]):
                a=len(words[i])*len(words[j])
                if a>result:
                    result=a
    return result

words = ["a","aa","aaa","aaaa"]
print(maxiMumPWL(words))

