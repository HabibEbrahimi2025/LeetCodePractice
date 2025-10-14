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
    prev=None
    minDist=float('inf')
    def helper(root):
        nonlocal prev,minDist
        if root:
            helper(root.left)
            if prev:
                minDist=min(minDist, root.val-prev)
            prev=root.val
            helper(root.right)
    helper(root)
    return minDist


        

arr = [90,69,None,49,89,None,52]
root=arrayToBST(arr)
print(minimumDistance(root))


