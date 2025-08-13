'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
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
        if not arr:
            return self.root
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
    
    def levelDisplay(self):
        que=deque([self.root])
        level=1
        while que:
            n=len(que)
            print(level)
            while n>0:
                node= que.popleft()
                print(node.val,end=' ')
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                n-=1
            print()
            level+=1
def hasPathSum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right:
        if (targetSum-root.val)==0:
            return True
        return False
    if hasPathSum(root.left, targetSum-root.val):
        return True
    if hasPathSum(root.right, targetSum-root.val):
        return True
    return False
root = []
targetSum = 0
ob=Solution()
ob.createByArray(root)
print(hasPathSum(ob.root, targetSum))
