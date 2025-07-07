def findOrginalStr(word, k):
    newWord=[]
    for ch in word:
        if ch not in newWord:
            newWord.append(ch)
    def checkInclude(word1):
        for ch in newWord:
            if ch not in word1:
                return False
        return True
    def backtracking(start, path, result,k,seen):
        if len(path)>=k:
            res=''.join(path)
            if res not in seen and checkInclude(res):
                seen.add(res)
                result[0]+=1
        
        for i in range(start, len(word)):
            path.append(word[i])
            backtracking(i+1, path, result, k, seen)
            path.pop()
    result=[0]
    seen=set()
    backtracking(0, [], result, k, seen)
    print(result[0])

word = "aabbccdd"
k=3
findOrginalStr(word, k)
    
