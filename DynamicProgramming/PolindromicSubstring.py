def polindromicSubstring(s):
    for i in range(len(s)):
        w=''
        for j in range(i, len(s)):
            w+=s[j]
            print(w, end=' ')
        print()
polindromicSubstring("ddidd")

def polindromicSub(s):
    def backtracking(start, path):
        print(''.join(path), end=' ')
        if start==len(s):
            return
        
        for i in range(start, len(s)):
            path.append(s[i])
            backtracking(i+1, path)
            path.pop()
    backtracking(0, [])

polindromicSub("abc")


