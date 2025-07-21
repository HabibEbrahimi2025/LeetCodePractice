class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def uniqeBinarySearchTree(n):
    if n==0:
        return 0
    
    def backtracking(start, end):
        trees = []

        if start>end:
            trees.append(None)
            return trees
        
        for number in range(start, end+1):
            left = backtracking(start, number-1)
            right = backtracking(number+1, end)
        
            for lef in left:
                for rig in right:
                    root = TreeNode(number)
                    root.left = lef
                    root.right = rig
                    trees.append(root)
        return trees
    return backtracking(1,n)


n=2
result=uniqeBinarySearchTree(n)
print(result)