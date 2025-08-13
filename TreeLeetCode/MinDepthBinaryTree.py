'''

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
'''
from collections import deque
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.left=left
        self.right=right
        self.val=value
class Solution():
    def __init__(self):
        self.root=None
    
    def createByArray(self,arr):
        self.root=TreeNode(arr[0])

        i=1
        que=deque([self.root])
        while que:
            node=que.popleft()
            
            if i<len(arr) and arr[i]:
                node.left=TreeNode(arr[i])
                que.append(node.left)
            i+=1
            if i<len(arr) and arr[i]:
                node.right=TreeNode(arr[i])
                que.append(node.right)
            i+=1
    def display(self, root):
        if root:
            print(root.val)
            self.display(root.left)
            self.display(root.right)
def minDepthBinary(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    depth=0
    que=deque([root])
    level=1
    controler=False
    while not controler and que:
        n=len(que)
        while n>0:
            node=que.popleft()
            if not node.left and not node.right:
                depth=level
                controler=True
                break
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            n-=1
        level+=1
    return depth

root = [2,None,3,None,4,None,5,None,6]
ob=Solution()
ob.createByArray(root)
# ob.display(ob.root)
print(minDepthBinary(ob.root))  