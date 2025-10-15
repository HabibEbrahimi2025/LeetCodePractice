'''

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
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
def leafSimilarTree(root1, root2):
    arr1=[]
    arr2=[]
    def bfs(root, holder):
        que=[root]
        while que:
            temp=que.pop()
            if not temp.left and not temp.right:
                holder.append(temp.val)
            if temp.left:
                que.append(temp.left)
            if temp.right:
                que.append(temp.right)
    bfs(root1,arr1)
    bfs(root2, arr2)
    return arr1==arr2
a = [1,2,3]
b = [1,3,2]
root1=arrayToTree(a)
root2=arrayToTree(b)
print(leafSimilarTree(root1, root2))
            