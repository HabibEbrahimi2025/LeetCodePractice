'''
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.

 

Example 1:

Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".
Example 2:
'''
def maximumRepeatingSubString(sequence, word):
    n=len(sequence)
    m=len(word)

    dp=[0]*n
    maxValue=0
    for i in range(m-1, n):
        if sequence[i-m+1: i+1] == word:
            if i>=m:
                dp[i]=dp[i-m]+1
            else:
                dp[i]=1
        maxValue=max(maxValue, dp[i])
    return maxValue


def maximumRepeatString(sequence, word):
    holder=""
    count=0
    for ch in sequence:
        holder+=ch
        if word in holder:
            count+=1
            holder=""
    return count



sequence = "aaba"
word = "b"
print(maximumRepeatingSubString(sequence, word))
#print(maximumRepeatingSubString(sequence, word))


