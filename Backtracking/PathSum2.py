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


            

