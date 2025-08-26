#constracting lps array 
def lpsArray(arr):
    n=len(arr)

    lps=[0]*n

    l=0
    i=1
    while i<n:
        if arr[l]==arr[i]:
            l+=1
            lps[i]=l
            i+=1
        else:
            if l!=0:
                l=lps[l-1]
            else:
                i+=1
    return lps

def KMP(pattern, word):
    lps=lpsArray(pattern)
    i=0
    j=0
    found=[]
    while i<len(word):
        if pattern[j]==word[i]:
            j+=1
            i+=1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
        if j==len(pattern):
            found.append(i-j)
            j=lps[j-1]
            
    print(found)


pattern='CABKAB'
word='ABCABKABLCABKAB'
KMP(pattern, word)