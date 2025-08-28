def findLongValid(s):
    close=0
    open=0

    maxLen=0
    for i in range(len(s)):
        if s[i]=='(':
            open+=1
        if s[i]==')':
            close+=1
        if open==close:
            maxLen=max(maxLen, close*2)
        if close>open:
            close=0
            open=0
    
    close1=0
    open1=0
    maxLen1=0
    for i in range(len(s)-1, -1,-1):
        if s[i]==')':
            close1+=1
        if s[i]=='(':
            open1+=1
        
        if open1==close1:
            maxLen1=max(maxLen1, open1*2)
        if open1>close1:
            open1=0
            close1=0
    print(maxLen)
    print(maxLen1)
    print(max(maxLen, maxLen1))

s='(()()((()()))'
findLongValid(s)


