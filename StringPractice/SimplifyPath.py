def simplifyPath(ss):
    parts=ss.split('/')
    stack=[]

    for part in parts:
        if part=='' or part=='.':
            continue

        elif part=='..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    res='/'+'/'.join(stack)
    return res
ss="/../"
print(simplifyPath(ss))