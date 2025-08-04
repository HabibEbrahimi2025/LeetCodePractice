def additiveNumber(num):
    for i in range(1,len(num)):
        for j in range(i+1, len(num)):
            a=num[:i]
            b=num[i:j]

            if len(a)>1 and a[0]=='0' or len(b)>0 and b[0]=='0':
                continue

            while j<len(num):
                sumAB=str(int(a)+int(b))
                lenSumAB=len(sumAB)

                if num[j:j+lenSumAB]==sumAB:
                    print('i ', i, ' j ', j, ' sumAb ', sumAB)
                if num[j:j+lenSumAB]!=sumAB:
                    break
                j+=lenSumAB

                a=b
                b=sumAB
            if j==len(num):
                return True
    return False

print(additiveNumber("199100199"))
