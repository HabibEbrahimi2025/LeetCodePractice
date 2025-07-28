
'''
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def generateTree(n):
    if n==0:
        return []
    
    def generator(start, end):
        trees=[]
        if start>end:
            return [None]
        for i in range(start, end+1):
            leftTree=generator(start, i-1)
            rightTree=generator(i+1, end)
            for left in leftTree:
                for right in rightTree:
                    root=TreeNode(i)
                    root.left= left
                    root.right=right
                    trees.append(root)
        return trees
    return generator(1,n)

def printTrees(tree):
    def helper(root):
        que= deque([root])

        while que:
            temp=que.popleft()
            print(temp.val, end=' ')

            if temp.left!=None:
                que.append(temp.left)
            if temp.right!=None:
                que.append(temp.right)
    for root in tree:
        print("New One")
        helper(root)
        
trees=generateTree(3)
printTrees(trees)