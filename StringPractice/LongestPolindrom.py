def checkPolindrom(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

def LongestPolindrom(s):
    finalRes=''
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if checkPolindrom(s[i:j+1]):
                if len(s[i:j+1])>len(finalRes):
                    finalRes=s[i:j+1]
    return finalRes
print(LongestPolindrom("aaaaaaaaaaaaaa"))



def longestPalindrome(s):
    if not s or len(s) == 1:
        return s

    start, end = 0, 0  # Store the start and end indices of the longest palindrome found

    for i in range(len(s)):
        # Odd-length palindrome
        len1 = expandAroundCenter(s, i, i)
        # Even-length palindrome
        len2 = expandAroundCenter(s, i, i+1)
        max_len = max(len1, len2)
        print("max ", max_len, " ", i)

        if max_len > (end - start):
            # Update the start and end indices
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end+1]

def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # Return the length of the palindrome
    return right - left - 1

print(longestPalindrome("aabcddcbaahhaa"))



