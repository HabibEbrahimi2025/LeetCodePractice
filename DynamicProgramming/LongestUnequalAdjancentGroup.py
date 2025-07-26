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