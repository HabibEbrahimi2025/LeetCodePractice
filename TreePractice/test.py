from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.children=[]

class Tree:
    def __init__(self, N):
        self.root=None
        self.N=N
    
    def setValue(self, value):
        newNode=Node(value)
        if self.root==None:
            self.root=newNode
            return
        
        que1=deque()
        que1.append(self.root)

        while que1:
            p= que1.popleft()

            if len(p.children)<self.N:
                p.children.append(newNode)
                return
            
            for ch in p.children:
                que1.append(ch)

    def display(self):
        if self.root is None:
            return
        que=deque()
        que.append(self.root)
        
        while que:
            p=que.popleft()
            print(p.data)

            for child in p.children:
                que.append(child)


t=Tree(3)
t.setValue(20)
t.setValue(25)
t.setValue(15)
t.setValue(10)
t.setValue(18)
t.setValue(30)
t.setValue(35)

t.display()

