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