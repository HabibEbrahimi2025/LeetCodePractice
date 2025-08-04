# Definition for a binary tree node.
'''


Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.root=None



    def setValue(self, node):
        if not node:
            return
        
        self.root=TreeNode(node[0])
        que=deque([self.root])

        i=1
        while que:
            current=que.popleft()

            if i<len(node) and node[i]!=None:
                newNode = TreeNode(node[i])
                current.left=newNode
                que.append(current.left)
            i+=1

            if i<len(node) and node[i]!=None:
                newNode2=TreeNode(node[i])
                current.right=newNode2
                que.append(current.right)

            i+=1

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

root = [1,2,3,None,5]
ob = Solution()
ob.setValue(root)
print(ob.binaryTreePaths(ob.root))
