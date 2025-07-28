
'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
'''
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class BinaryTree:
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
    def display(self, node):
        if not node:
            return
        
        print(node.val)
        if node.left ==None and node.right==None:
            print("hi")

        self.display(node.left) 
        self.display(node.right)
    
    def targetSumNode(self, root, targetSum):
        result=[]
        def backtracking(node, path, currentSum):
            if not node:
                return
            path.append(node.val)
            currentSum+=node.val

            if not node.left and not node.right and currentSum==targetSum:
                result.append(path[:])
            backtracking(node.left, path, currentSum)
            backtracking(node.right, path, currentSum)
            path.pop()
        backtracking(root, [], 0)
        return result


root = [5,4,8,11,None,13,4,7,2,None,None,5,1]
target=22
ob=BinaryTree()
ob.setValue(root)
print(ob.targetSumNode(ob.root, 22))


            

