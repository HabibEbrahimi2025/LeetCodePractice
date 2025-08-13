'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,null,3,null,3]
Output: false
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
    

def isSymmetric2(root):
    def helper(leftSide, rightSide):
        if not leftSide and not rightSide:
            return True
        if not leftSide and rightSide:
            return False
        if leftSide and not rightSide:
            return False
        if leftSide.val != rightSide.val:
            return False
        
        return helper(leftSide.left, rightSide.right) and helper(leftSide.right, rightSide.left)
    return helper(root, root)


root = [1,2,2,3,4,4,3]
ob=Solution()
ob.createByArray(root)
print(isSymmetric2(ob.root))
