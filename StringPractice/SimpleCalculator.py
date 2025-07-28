'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
'''
class Solution:
    def calculate(self, s: str) -> int:
        MinVal=(-2)**31
        MaxVal=(2)**32-1
        s2=''
        flag=0
        for c in s:
            if c=='-' or c=='+' or c=='*' or c=='/':
                flag=1
            if c==' ':
                continue
            else:
                s2+=c
        if flag==0:
            return int(s)
        def checkState(a,b):
            if (a=='-' or a=='+' )and (b=='*' or b=='/'):
                return True
            else:
                return False
        def doOperation(a,b, op):
            if op=='+':
                return a+b
            elif op=='-':
                return a-b
            elif op=='*':
                return a*b
            else:
                return int(a/b)
            
        element=[]
        operator=[]

        i=0
        while i<len(s2):
            if s2[i].isdigit():
                e=''
                while i<len(s2) and s2[i].isdigit():
                    e+=s2[i]
                    i+=1
                element.append(int(e))
            else:
                if not operator:
                    operator.append(s2[i])
                    i+=1
                elif checkState(operator[len(operator)-1], s2[i]):
                    op=s2[i]
                    i+=1
                    ee=''
                    while i<len(s2) and  s2[i].isdigit():
                        ee+=s2[i]
                        i+=1
                    a=doOperation(element.pop(), int(ee), op)
                    element.append(a)
                else:
                    bb=element.pop()
                    aa=element.pop()
                    b=doOperation(aa,bb, operator.pop())
                    element.append(b)
                    operator.append(s2[i])
                    i+=1
        while operator:
            dd=element.pop()
            cc=element.pop()
            res=doOperation(cc,dd, operator.pop())
            element.append(res)
        finalValue=int(element[0])
        if MinVal<=finalValue<=MaxVal:
            return int(element[0])
        elif finalValue<MinVal:
            return MinVal
        else:
            return MaxVal