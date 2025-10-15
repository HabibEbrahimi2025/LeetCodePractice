'''
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
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
def increasingBST(self, root):
    root2=None
    def helper(value):
        nonlocal root2
        if not root2:
            root2=TreeNode(value)
        else:
            current=root2
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
    def inOrder(root):
        if root:
            inOrder(root.left)
            helper(root.val)
            inOrder(root.right)
    inOrder(root)
    return root2

a = [5,3,6,2,4,None,8,1,None,None,None,7,9]
root=arrayToBST(a)
res=increasingBST(root)

