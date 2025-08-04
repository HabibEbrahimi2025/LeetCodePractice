'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]
'''
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
    

