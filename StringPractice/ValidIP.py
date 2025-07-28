'''
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
'''
def validIP(s):
    def backtraking(start,path,res):
        if len(path)==4:
            if start==len(s):
                res.append('.'.join(path))
            return
        
        for length in range(1,4):
            if start+length>len(s):
                break

            seg=s[start:start+length]


            if (seg.startswith('0') and len(seg)>1) or int(seg)>255:
                continue
            backtraking(start+length, path+[seg],res)
    res=[]
    path=[]
    backtraking(0, path, res)
    return res
print(validIP("0000"))