'''
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
'''
from collections import deque
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.left=left
        self.right=right
        self.val=value

def arrayToBST(arr):
    root=None
    def helper(value):
        nonlocal root
        if not root:
            root=TreeNode(value)
        else:
            current=root
            parent=current
            while current:
                if value>=current.val:
                    parent=current
                    current=current.right
                else:
                    parent=current
                    current=current.left
            if value>=parent.val:
                parent.right=TreeNode(value)
            else:
                parent.left=TreeNode(value)
    for val in arr:
        if val:
            helper(val)
    return root

def twoSumInput(root, k):
    holder=[]
    def inOrder(root):
        if root:
            inOrder(root.left)
            holder.append(root.val)
            inOrder(root.right)
    inOrder(root)
    for i in range(len(holder)-1):
        for j in range(i+1, len(holder)):
            finalRes=holder[i]+holder[j]
            if finalRes==k:
                return True
    return False

arr=[5,3,6,2,4,None,7]
root=arrayToBST(arr)
print(twoSumInput(root, 28))           
