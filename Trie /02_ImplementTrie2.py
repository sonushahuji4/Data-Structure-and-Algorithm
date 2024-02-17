# Link : https://www.codingninjas.com/studio/problems/implement-trie_1387095?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.wordCount = 0
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        temp = self.root
        for ch in word:
            charIndex = ord(ch) - ord('a')
            if temp.children[charIndex] == None:
                child = TrieNode()
                temp.children[charIndex] = child
            temp = temp.children[charIndex]
            temp.wordCount += 1
        temp.isEndOfWord = True

    def countWordsEqualTo(self, word):
        temp = self.root
        index = -1
        for ch in word:
            charIndex = ord(ch) - ord('a')
            index = charIndex
            if temp.children[charIndex] == None: return 0
            temp = temp.children[charIndex]
        return temp.wordCount

    def countWordsStartingWith(self, prefix):
        temp = self.root
        for ch in prefix:
            charIndex = ord(ch) - ord('a')
            if temp.children[charIndex] != None:
                temp = temp.children[charIndex]
        if not temp.isEndOfWord: return temp.wordCount
        return 0

    def erase(self, word):
        temp = self.root
        for ch in word:
            charIndex = ord(ch) - ord('a')
            if temp.children[charIndex] != None:
                temp = temp.children[charIndex]
                temp.wordCount -= 1
