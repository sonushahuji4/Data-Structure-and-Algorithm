# Link : https://leetcode.com/problems/word-search-ii/description/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = ""
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ans = []
        self.direction = [(1,0),(-1,0),(0,1),(0,-1)]
    
    def insert(self, word):
        temp = self.root
        for ch in word:
            charIndex = ord(ch) - ord('a')
            if temp.children[charIndex] == None:
                child = TrieNode()
                temp.children[charIndex] = child
            temp = temp.children[charIndex]
        temp.word = word
        temp.isEndOfWord = True
    
    def search(self, board, i, j, temp,m,n):

        if i < 0 or i >= m or j < 0 or j >= n: return
        charIndex = ord(board[i][j]) - ord('a')
        if board[i][j] == '$' or temp.children[charIndex] == None: return 
        temp = temp.children[charIndex]
        if temp.isEndOfWord:
            self.ans.append(temp.word)
            temp.isEndOfWord = False
        
        char = board[i][j]
        board[i][j] = '$'
        for x, y in self.direction:
            dx = x + i
            dy = y + j
            self.search(board, dx, dy, temp,m,n)
        board[i][j] = char

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for eachWord in words:
            trie.insert(eachWord)

        m = len(board)
        n = len(board[0])
        
        temp = trie.root
        for i in range(m):
            for j in range(n):
                charIndex = ord(board[i][j]) - ord('a')
                if temp.children[charIndex] != None:
                    trie.search(board, i, j, temp,m,n)
    
        return trie.ans
