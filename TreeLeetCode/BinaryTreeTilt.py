'''
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.

 

Example 1:


Input: root = [1,2,3]
Output: 1
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
def binaryTreeTilt(root):
    finalRes=0
    def helper(node):
        nonlocal finalRes
        if not node:
            return 0
        leftSide=helper(node.left)
        rightSide=helper(node.right)
        finalRes+=abs(leftSide-rightSide)
        return leftSide+rightSide+node.val
    helper(root)
    return finalRes

arr=[4,2,9,3,5,None,7]
root=arrayToTree(arr)
print(binaryTreeTilt(root))
