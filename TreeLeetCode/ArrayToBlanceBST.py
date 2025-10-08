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



def arrayToBST(arr):
    root=None
    def helper(value):
        nonlocal root
        if not root:
            root=TreeNode(value)
        else:
            current=root
            parent=current
            while current:
                if value>=current.val:
                    parent=current
                    current=current.right
                else:
                    parent=current
                    current=current.left
            if value>=parent.val:
                parent.right=TreeNode(value)
            else:
                parent.left=TreeNode(value)
    for val in arr:
        if val:
            helper(val)
    return root

def arrayToBSTBlanced(nums):
    def helper(left, right):
        if left>right:
            return None
            
        midVal=(left+right)//2
        root=TreeNode(nums[midVal])
        root.left=helper(left, midVal-1)
        root.right=helper(midVal+1, right)
        return root
    return helper(0, len(nums)-1)

def countChild(root):
    childCounter={}

    def counter(root):
        if not root:
            return 0
        
        count=1
        count+=counter(root.left)
        count+=counter(root.right)
        childCounter[root.val]=count
        return count
    counter(root)
    print(childCounter)

def leftLeave(root):
    fianlRes=[0]
    def helper(root, state):
        if root:
            if not root.left and not root.right and state:
                fianlRes[0]+=root.val
            
            helper(root.left, True)
            helper(root.right, False)
    if not root:
        return 0
    helper(root, False)
    return fianlRes[0]


            



def preOrder(root):
    arr=[]
    def helper(root):
        if root:
            
            helper(root.left) 
            helper(root.right)
            arr.append(root.val)
    helper(root)
    if len(arr)<=1:
        return 0
    arr.sort()
    minValue=float('inf')
    for i in range(1,len(arr)):
        if arr[i]-arr[i-1]<minValue:
            minValue=arr[i]-arr[i-1]
    return minValue

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)

arr = [4]

def maxDiameter(root):
    maxDiameter=0

    def helper(node):
        nonlocal maxDiameter
        if not node:
            return 0
        left=helper(node.left)
        right=helper(node.right)

        maxDiameter=max(maxDiameter, left+right)
        return 1+(max(left, right))
    helper(root)
    return maxDiameter
arr=[1,2,3,4,5]



#root1=arrayToTree(arr2)
root=arrayToTree(arr)
print(maxDiameter(root))
# countChild(root1)
#print(leftLeave(root1))
                    