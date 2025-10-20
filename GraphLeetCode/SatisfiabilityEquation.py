'''
You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

 

Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
'''
def satifiability(equations):
    parent={chr(i):chr(i) for i in range(ord('a'), ord('z')+1)}
    def find(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    def union(a,b):
        parent[find(a)]=find(b)
    for s in equations:
        if s[1:3]=='==':
            union(s[0], s[3])
    for s in equations:
        if s[1:3]=='!=':
            if find(s[0])==find(s[3]):
                return False
    return True

equations = ["a==b","c=a"]
print(satifiability(equations))