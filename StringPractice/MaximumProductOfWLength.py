'''
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

 

Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
'''
def maxiMumPWL(words):
    if len(words)<=1:
        return 0
    
    def checkPair(a,b):
        for ch in b:
            if ch in a:
                return False
        return True
    
    result=0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if checkPair(words[i], words[j]):
                a=len(words[i])*len(words[j])
                if a>result:
                    result=a
    return result

words = ["a","aa","aaa","aaaa"]
print(maxiMumPWL(words))

