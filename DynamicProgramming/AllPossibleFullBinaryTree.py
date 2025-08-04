
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def allPossibleFBT(n):
    memo = {}
    def helper(n):
        if n in memo:
            return memo[n]
        if n == 1:
            return [TreeNode(0)]
        result = []
        for left_nodes in range(1, n, 2): 
            right_nodes = n - 1 - left_nodes
            for left in helper(left_nodes):
                for right in helper(right_nodes):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    result.append(root)
        memo[n] = result
        return result
    return helper(n)
trees = allPossibleFBT(5)
print(len(trees)) 
