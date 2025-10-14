from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val=val
        self.children=[]
def createNArrayTree(arr):
    root=TreeNode(arr[0])
    que=deque([root])
    k=1
    while que:
        temp=que.popleft()
        child=[]
        for i in range(3):
            if k<len(arr) and arr[k]:
                ch=TreeNode(arr[k])
                child.append(ch)
                que.append(ch)
            k+=1
        temp.children=child[:]
    return root


def build_nary_tree(arr):
    if not arr:
        return None 
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 2
    
    while i < len(arr):
        parent = queue.popleft()
        while i < len(arr) and arr[i] is not None:
            child = TreeNode(arr[i])
            parent.children.append(child)
            queue.append(child)
            i += 1
        i += 1 
    return root

def levelOrder(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        level_values = []
        next_queue = []
        for node in queue:
            level_values.append(node.val)
            for child in node.children:
                next_queue.append(child)
        result.append(level_values)
        queue = next_queue
    return result

def maxHeight(root):
    maxH=0
    def helper(root, level):
        nonlocal maxH
        if not root:
            return 0
        if len(root.children)==0:
            maxH=max(maxH, level)
            return 0
        for node in root.children:
            level+=1
            helper(node, level)
            level-=1
    helper(root, 1)
    print(maxH)

ar=[1,None,3,2,4,None,5,6]
arr = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
root=build_nary_tree(ar)
maxHeight(root)



    



