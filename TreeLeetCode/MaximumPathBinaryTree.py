'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
'''
from collections import deque
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.left=left
        self.right=right
        self.val=value
class Solution():
    def __init__(self):
        self.root=None
    
    def createByArray(self,arr):
        self.root=TreeNode(arr[0])

        i=1
        que=deque([self.root])
        while que:
            node=que.popleft()
            
            if i<len(arr) and arr[i]:
                node.left=TreeNode(arr[i])
                que.append(node.left)
            i+=1
            if i<len(arr) and arr[i]:
                node.right=TreeNode(arr[i])
                que.append(node.right)
            i+=1
    def display(self, root):
        if root:
            print(root.val)
            self.display(root.left)
            self.display(root.right)


def display2(root):
    if not root:
        return 0
    leftSide=display2(root.left)
    rightSide=display2(root.right)
    return 1+max(leftSide, rightSide)
root = [3,9,20,None,None,15,7]
ob=Solution()
ob.createByArray(root)
print(display2(ob.root))
