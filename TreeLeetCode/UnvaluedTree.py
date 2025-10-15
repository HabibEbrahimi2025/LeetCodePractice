'''
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

 

Example 1:


Input: root = [1,1,1,1,1,null,1]
Output: true
'''
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

def unValuedTree(root):
    holder=None
    isUnvalue=True
    def inOrder(root):
        nonlocal isUnvalue, holder
        if root:
            inOrder(root.left)
            if holder:
                if holder!=root.val:
                    isUnvalue=False
                    return
            holder=root.val
            inOrder(root.right)
    inOrder(root)
    return isUnvalue
arr=[1,1,1,1,1,None,1]
root=arrayToTree(arr)
print(unValuedTree(root))


