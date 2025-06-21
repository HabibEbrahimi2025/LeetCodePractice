class Trie:
    def __init__(self):
        self.holder=[]
    def insert(self, word: str) -> None:
        self.holder.append(word)

    def search(self, word: str) -> bool:
        if word in self.holder:
            return True
        else:
            return False        

    def startsWith(self, prefix: str) -> bool:
        flag=False
        for item in self.holder:
            if item.startsWith(prefix):
                flag=True
        return flag
    

