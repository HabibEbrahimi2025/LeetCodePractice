'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
'''
def reverseWord(s):
    s=s.strip()
    res=s.split(' ')
    finalRes=[]
    def backtracking(index):
        if index==len(res):
            return
        backtracking(index+1)
        if res[index]!='':
            finalRes.append(res[index])
    backtracking(0)
    result=" ".join(finalRes)
    return result
        
s="a good   example"
print(reverseWord(s))
    