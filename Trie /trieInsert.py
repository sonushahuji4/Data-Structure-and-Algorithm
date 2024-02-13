class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        temp = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if temp.children[index] == None:
                child = TrieNode()
                temp.children[index] = child
            temp = temp.children[index]
        temp.isEndOfWord = True

    def search(self, word: str) -> bool:
        temp = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if temp.children[index] == None: return False
            temp = temp.children[index]
        return temp.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if temp.children[index] == None: return False
            temp = temp.children[index]
        return True
