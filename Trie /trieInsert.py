class TrieNode:
  def __init__(self):
    self.children = [None]*26
    self.isEndOfWord = False
    
class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self,word):
    temp = self.root
    for eachChar in word:
      charIndex = ord(eachChar) - ord('a')
      if temp.children[charIndex] == None:
        child = TrieNode()
        temp.children[charIndex] = child
      temp = temp.children[charIndex]
    temp.isEndOfWord = True

  def search(self,word):
    temp = self.root
    for eachChar in word:
      charIndex = ord(eachChar) - ord('a') 
      if temp.children[charIndex] == None: return False
      temp = temp.children[charIndex]
    return temp.isEndOfWord
    
