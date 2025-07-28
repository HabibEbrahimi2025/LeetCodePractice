'''
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''
def LongestSubSringWithoutRepeatC(s):
    ss=set()
    finalLenth=0
    i=0
    for j in range(len(s)):
        while s[j] in ss:
            ss.remove(s[i])
            i+=1
        ss.add(s[j])
        if (n:=j-i+1)>finalLenth:
            finalLenth=n
    return finalLenth
print(LongestSubSringWithoutRepeatC("bbbbb"))