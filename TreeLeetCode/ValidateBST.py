'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
'''
from collections import deque
import math
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


def validBST(root):
    if not root.left and not root.right:
        return False
    que=deque([(root, -math.inf, math.inf)])
    while que:
        node, low, high=que.popleft()
        if not (low<node.val<high):
            return False
        if node.left:
            que.append((node.left, low, node.val))
        if node.right:
            que.append((node.right, node.val, high))
    return True

def validBST2(root):
    def helper(root, low, high):
        if not root:
            return True
        
        if not(low<root.val<high):
            return False
        
        return helper(root.left, low, root.val) and helper(root.right, root.val, high)
    return helper(root,-math.inf, math.inf)

root = [5,4,6,None,None,3,7]
ob=Solution()
ob.createByArray(root)

print(validBST2(ob.root))