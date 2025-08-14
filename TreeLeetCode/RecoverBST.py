''''
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
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

def recoverBST(root):
    prev=first=second=None

    def inOrder(root):
        if not root:
            return
        nonlocal prev,first,second

        inOrder(root.left)

        if prev and prev.val>root.val:
            if not first:
                first=prev
            second=root
        prev=root

        inOrder(root.right)
    inOrder(root)
    if first and second:
        first.val, second.val = second.val, first.val
    

root = [3,1,4,None,None,2]
ob=Solution()
ob.createByArray(root)

ob.levelDisplay()
recoverBST(ob.root)
print("After edit ")
ob.levelDisplay()