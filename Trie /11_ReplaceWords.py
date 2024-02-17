# Link : https://leetcode.com/problems/replace-words/description/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = ""
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        temp = self.root
        for char in word:
            charIndex = ord(char) - ord('a')
            if temp.children[charIndex] == None:
                child = TrieNode()
                temp.children[charIndex] = child
            temp = temp.children[charIndex]
        temp.word = word
        temp.isEndOfWord = True
    
    def replaceWord(self,word):
        temp = self.root
        for char in word:
            charIndex = ord(char) - ord('a')
            if temp.children[charIndex] == None: return [False,""]
            temp = temp.children[charIndex]
            if temp.isEndOfWord: return [temp.isEndOfWord, temp.word]  
        return [False,""]

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        copiedSentence = sentence.split(" ")
        copiedSentenceLenght = len(copiedSentence)
        for i in range(copiedSentenceLenght):
            isExsit, word = trie.replaceWord(copiedSentence[i])
            if isExsit:
                copiedSentence[i] = word
        return " ".join(copiedSentence)
      
