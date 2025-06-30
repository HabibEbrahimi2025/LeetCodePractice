# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root):
        def backtracking(Node, path, allPath):
            if Node!=None:
                if Node.left==None and Node.right==None:
                    path.append(str(Node.val))
                    a="->".join(path)
                    allPath.append(a)
                    path.pop()
                path.append(str(Node.val))
                backtracking(Node.left, path, allPath)
                backtracking(Node.right, path, allPath)
                path.pop()
        res=[]
        backtracking(root, [], res)
        return res