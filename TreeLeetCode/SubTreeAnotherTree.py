'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
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

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not subRoot:
        return True
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

def isSameTree(s: TreeNode, t: TreeNode) -> bool:
    if not s and not t:
        return True
    if not s or not t or s.val != t.val:
        return False
    return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
        
def findSubTree(root, subRoot):
    def isSub(root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        if isSame(root, subRoot):
            return True
        
        return isSub(root.left, subRoot) or isSub(root.right, subRoot)
    def isSame(parent, child):
        if not parent and not child:
            return True
        if not parent or not child or parent.val!=child.val:
            return False
        return isSame(parent.left, child.left) and isSame(parent.right, child.right)
    return isSub(root, subRoot)

arr=[3,4,5,1,2]
subArr = [4,1,2]

root=arrayToTree(arr)
subRoot=arrayToTree(subArr)
print(findSubTree(root, subRoot))

