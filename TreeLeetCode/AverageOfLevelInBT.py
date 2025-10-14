from collections import deque
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.left=left
        self.right=right
        self.val=value
def arrayToTree(arr):
    root=TreeNode(arr[0])
    que=deque([root])
    i=1
    while que:
        temp=que.popleft()
        if i<len(arr) and arr[i]:
            temp.left=TreeNode(arr[i])
            que.append(temp.left)
        i+=1
        if i<len(arr) and arr[i]:
            temp.right=TreeNode(arr[i])
            que.append(temp.right)
        i+=1
    return root

def averageLevel(root):
    result=[]
    que=deque([root])

    while que:
        n=len(que)
        x=n
        holder=0
        while n>0:
            temp=que.popleft()
            holder+=temp.val

            if temp.left:
                que.append(temp.left)
            if temp.right:
                que.append(temp.right)
            n-=1
        result.append(round(holder/x, 5))
    return result

arr = [3,9,20,None,None,15,7]
root=arrayToTree(arr)
print(averageLevel(root))


