class Node:
    def __init__(self):
        self.children=dict()
        self.isEnd=False

class Trie:
    def __init__(self):
        self.root=Node()
    
    def insertValue(self,word):
        curentNode=self.root

        for val in word:
            if val not in curentNode.children:
                curentNode.children[val]=Node()
            curentNode=curentNode.children[val]
        curentNode.isEnd=True
    def search(self, word):
        currentNode=self.root

        for val in word:
            if val not in currentNode.children:
                return False
            currentNode=currentNode.children[val]
        return currentNode.isEnd

    def delete(self, word):
        self._delete(self.root, word, 0)

    def _delete(self, currentNode, word, index):
        if index==len(word):
            if not currentNode.isEnd:
                return False
            currentNode.isEnd=False

            return len(currentNode.children)==0

        c=word[index]
        node=currentNode.children.get(c)
        if node is None:
            return False
        
        delete_current_node=self._delete(node, word, index+1)
        if delete_current_node:
            del currentNode.children[c]
            return len(currentNode.children)==0 and not currentNode.isEnd
        return False

    def has_prefix(self, prefix):
        currentNode=self.root

        for val in prefix:
            if val not in currentNode.children:
                return False
            currentNode=currentNode.children[val]
        return True
    def startsWith(self, prefix):
        words=[]
        currentNode=self.root

        for c in prefix:
            if c not in currentNode.children:
                return False
            currentNode=currentNode.children[c]
        def _dfs(currentNode, path):
            if currentNode.isEnd:
                words.append(''.join(path))
            for c, childNode in currentNode.children.items():
                _dfs(childNode, path+[c])
        _dfs(currentNode, list(prefix))

        return words
    def listWord(self):
        words=[]

        def _dfs(currentNode, path):
            if currentNode.isEnd:
                words.append(''.join(path))
            for c, childNode in currentNode.children.items():
                _dfs(childNode, path+[c])
        _dfs(self.root, [])
        return words

trie=Trie()
trie.insertValue('hello')
trie.insertValue('henry')
trie.insertValue('mike')
trie.insertValue('minimal')
trie.insertValue('minimum')

print(trie.listWord())
print(trie.has_prefix('mi'))
print(trie.startsWith('mi'))
trie.delete('minimal')
print(trie.listWord())
print(trie.search('mike'))
print(trie.search('minimal'))
trie.insertValue('mini')
print(trie.listWord())


    
            