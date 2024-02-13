class TrieNode:
  def __init__(self):
    self.children = [None]*26
    self.isEndOfWord = False
    
class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self,word):
    temp = self.root
    for eachWord in word:
      charIndex = ord(word)-ord('a')
      if temp.children[charIndex] == None:
        child = TrieNode()
        temp.children[charIndex] = child
      temp = temp.children[charIndex]
    temp.isEndOfWord = True
    
