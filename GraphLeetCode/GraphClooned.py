from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.node = None
        self.nodes_map = {}  # keeps track of created nodes
    
    def createGraph(self, adjList):
        if not adjList:
            return None
        
        for i in range(1, len(adjList)+1):
            self.nodes_map[i]=Node(i)
        
        for i , neighbors in enumerate(adjList, 1):
            self.nodes_map[i].neighbors=[self.nodes_map[nx] for nx in neighbors]
        
        self.node=self.nodes_map[1]
        return self.node
    

   
    def display(self, node):
        que=deque([node])
        seen=set()
        seen.add(node.val)
        while que:
            node = que.popleft()
            print(node.val ,' => ')
            for child in node.neighbors:
                print(child.val, end=' ')
                if child.val not in seen:
                    seen.add(child.val)
                    que.append(child)
            print()
    
            
    def cloneGraph(self, node):
        newNode=None
        newMap={}
        que=deque([node])
        seen=set()
        seen.add(node.val)
        while que:
            temp = que.popleft()
            newMap[temp.val]=Node(temp.val)
            for child in temp.neighbors:
                newMap[temp.val].neighbors.append(child)
                
                if child.val not in seen:
                    seen.add(child.val)
                    que.append(child)
        newNode=newMap[1]
        return newNode

    def cloneGraph2(self,node):
        if not node:
            return None
        
        visited = {}
        visited[node] = Node(node.val, [])

        queue = deque([node])

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        
        return visited[node]
    


# Example
adjList = [[2,4],[1,3],[2,4],[1,3]]
ob = Solution()
ob.createGraph(adjList)
#ob.display(ob.node)
newNode=ob.cloneGraph2(ob.node)
