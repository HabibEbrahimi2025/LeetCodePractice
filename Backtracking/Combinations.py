def combine(n, k):
    if n==0:
        return 0
    def backtracking(start, word, path, allPath):
        if len(path)==k:
            allPath.append(path[:])
            return
        for i in range(start, len(word)):
            path.append(word[i])
            backtracking(i+1, word, path, allPath)
            path.pop()
    word=[x for x in range(1,n+1)]
    allPath=[]
    backtracking(0, word, [], allPath)
    return allPath
n=1
k=1
combine(n,k)