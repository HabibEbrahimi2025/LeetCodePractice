
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


