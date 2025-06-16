def reverseWord(s):
    s=s.strip()
    res=s.split(' ')
    finalRes=[]
    def backtracking(index):
        if index==len(res):
            return
        backtracking(index+1)
        if res[index]!='':
            finalRes.append(res[index])
    backtracking(0)
    result=" ".join(finalRes)
    return result
        
s="a good   example"
print(reverseWord(s))
    