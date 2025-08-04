'''

You are given a string array words and a binary array groups both of length n.

A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements at the same indices in groups are different (that is, there cannot be consecutive 0 or 1).

Your task is to select the longest alternating subsequence from words.

Return the selected subsequence. If there are multiple answers, return any of them.

Note: The elements in words are distinct.

 

Example 1:

Input: words = ["e","a","b"], groups = [0,0,1]

Output: ["e","b"]
'''
def longestUnequalAdjacentGroup(words, groups):
    result=[]

    for i in range(len(words)):
        res=[]
        res.append(words[i])
        for j in range(i+1, len(words)):
            if groups[j]!=groups[j-1]:
                res.append(words[j])
        if len(res)>len(result):
            result=res
    return result


def longestUnequalDynamic(words, groups):
    result=[]
    result.append(words[0])
    for i in range(1,len(words)):
        if groups[i]!=groups[i-1]:
            result.append(words[i])
    return result

words = ["a","b","c","d"]
groups = [1,0,1,1]

#print(longestUnequalAdjacentGroup(words, groups))
print(longestUnequalDynamic(words, groups))