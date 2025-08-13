'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
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
            i+=1
            if i<len(arr) and arr[i]:
                node.right=TreeNode(arr[i])
            i+=1
    
    def levelDisplay(self):
        que=deque([self.root])

        level=1
        while que:
            n=len(que)
            print(level)
            while n>0:
                node= que.popleft()
                print(node.val,end=' ')
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                n-=1
            print()
            level+=1
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
p = [1,2,3]
q = [1,2,3]
ob1=Solution()
ob1.createByArray(p)
ob1.levelDisplay()
print("The second part")
ob2=Solution()
ob2.createByArray(q)
ob2.levelDisplay()

print(isSameTree(ob1.root, ob2.root))


