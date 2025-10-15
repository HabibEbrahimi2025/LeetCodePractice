'''
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

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
        if i<len(arr) and arr[i]!=None:
            temp.left=TreeNode(arr[i])
            que.append(temp.left)
        i+=1
        if i<len(arr) and arr[i]!=None:
            temp.right=TreeNode(arr[i])
            que.append(temp.right)
        i+=1
    return root

def sumOfRootToLeaf(root):
    finalRes=0
    def inOrder(root, path):
        nonlocal finalRes
        if root:
            path.append(str(root.val))
            if not root.left and not root.right:
                res=''.join(path)
                finalRes+=int(res,2)
            inOrder(root.left, path)
            inOrder(root.right, path)
            path.pop()
    inOrder(root, [])
    return finalRes

arr = [1,0,1,0,1,0,1]
root=arrayToTree(arr)
print(sumOfRootToLeaf(root))
            