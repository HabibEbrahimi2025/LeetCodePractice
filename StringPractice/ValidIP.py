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