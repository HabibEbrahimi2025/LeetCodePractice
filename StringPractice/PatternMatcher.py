def findMatcher(symbol, s):
    x=symbol.count('x')
    y=symbol.count('y')

    yRes=''
    xRes=''
    if y>x:
        for i in range(len(s)):
            j=i+1
            while j<len(s):
                sub=s[i:j]
                if s.count(sub)>=y:
                    j+=1
                    if len(sub)>len(yRes):
                        yRes=sub
                else:
                    break
    else:
        for i in range(len(s)):
            j=i+1
            while j<len(s):
                sub=s[i:j]
                if s.count(sub)>=x:
                    j+=1
                    if len(sub)>len(xRes):
                        xRes=sub
                else:
                    break
    ss=s.split(xRes)
    print(ss)

    print(yRes if len(yRes)>0 else xRes)
    


symblol='xxyxxy'
s='gogopowerrangergogopowerranger'

findMatcher(symblol, s)
