def maxScoreFromRemoving(s, x, y):

    def remover(s, first, second, value):
        stack=[]
        res=0

        for ch in s:
            if stack and stack[-1]==first and ch==second:
                stack.pop()
                res+=value
            else:
                stack.append(ch)
        return ''.join(stack), res
    

    res1=0
    res2=0
    if x>y:
        s, res1=remover(s, 'a', 'b', x)
        s , res2 = remover(s, 'b', 'a', y)
    else:
        s, res1=remover(s, 'b', 'a', y)
        s , res2 = remover(s, 'a', 'b', x)
    return res1+res2

s = "aabbaaxybbaabb"
x = 5
y = 4

print(maxScoreFromRemoving(s, x, y))

