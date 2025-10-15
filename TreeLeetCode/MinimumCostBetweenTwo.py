'''
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
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
# def minimumDistance(root):
#     minDist=float('inf')
#     def helper(root):
#         nonlocal minDist
#         if not root:
#             return 0
#         if not root.left and not root.right:
#             return root.val
#         leftSide=helper(root.left)
#         rightSide=helper(root.right)
#         minValue=abs(leftSide-rightSide)
#         minValue=min(minValue, abs(leftSide-root.val))
#         minValue=min(minValue, abs(rightSide-root.val))
#         minDist=min(minValue, minDist)
#         return root.val
#     helper(root)
#     return minDist

def minimumDistance(root):
    holder=[]
    def helper(root):
        if root:
            helper(root.left)
            holder.append(root.val)
            helper(root.right)
    helper(root)
    minDist=float('inf')
    for i in range(len(holder)-1):
        for j in range(i+1, len(holder)):
            minDist=min(abs(holder[i]-holder[i+1]), minDist)
    return minDist


        

arr = [90,69,None,49,89,None,52]
root=arrayToBST(arr)
print(minimumDistance(root))


