# def myAtio(s):
#     if s[0]!=' ' and s[0]!='-' and not s[0].isdigit():
#         return 0
#     res=''

#     for i in range(len(s)):
#         if s[i]==' ':
#             continue

#         if len(res)==0 and s[i]=='-':
#             res+=res.join(s[i])
#         elif s[i].isdigit():
#             res+=res.join(s[i])  
#         else:
#             if len(res)!=0:
#                 return res
#             else:
#                 return 0
#     return res

# ss=' -123rt456'
# print(myAtio(ss))

class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # 1. Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow before adding digit
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1

        return sign * num

ob=Solution()
print(ob.myAtoi(" +42"))