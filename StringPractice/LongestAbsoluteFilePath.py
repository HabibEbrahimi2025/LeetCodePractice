def longestAbsoluteFilePath(input):
    maxLen=0
    maxLenDepth={0:0}

    for line in input.split('\n'):
        depth=line.count('\t')
        name=line.lstrip('\t')

        if '.' in name:
            maxLen=max(maxLen, maxLenDepth[depth]+len(name))
        else:
            maxLenDepth[depth+1]=maxLenDepth[depth]+len(name)+1
    return maxLen
input =  "a"
print(longestAbsoluteFilePath(input))
