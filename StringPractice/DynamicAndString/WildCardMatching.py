def isMatch(s, p):
    def match(i, j):
        # Base cases
        if i == 0 and j == 0:
            return True
        if j == 0:
            return False
        if i == 0:
            return all(p[k] == '*' for k in range(j))
        if p[j - 1] == s[i - 1] or p[j - 1] == '?':
            return match(i - 1, j - 1)
        if p[j - 1] == '*':
            return match(i, j - 1) or match(i - 1, j)

        return False

    return match(len(s), len(p))
s='adceb'
p='*a*b'
print(isMatch(s,p))
