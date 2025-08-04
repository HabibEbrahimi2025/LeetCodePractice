
def removeDuplicate(s):
    if len(s)<=1:
        return s
    def checkUniqness(ss):
        check=set()
        for ch in ss:
            if ch in check:
                return False
            check.add(ch)
        return True
    def backtraking(start, count, path, result):
        if len(path)==count:
            a=''.join(path)
            
            if (result[0]=='') or (checkUniqness(a) and a<result[0]):
                result[0]=a
            return
        for i in range(start, len(s)):
            path.append(s[i])
            backtraking(i+1, count, path, result)
            path.pop()
    seen=set()
    count=0
    for ch in s:
        if ch not in seen:
            count+=1
            seen.add(ch)
    result=['']
    path=[]
    backtraking(0, count, path, result)
    print(result[0])

s='bcabc'
removeDuplicate(s)
