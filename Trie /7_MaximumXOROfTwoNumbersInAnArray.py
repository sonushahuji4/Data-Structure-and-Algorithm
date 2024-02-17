# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None] * 2

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,num):
        temp = self.root
        for i in range(31, -1, -1):
            bit = ((num >> i) & 1)
            if temp.children[bit] == None
                temp.children[bit] = TrieNode()
            temp = temp.children[bit]
    
    def getMax(self,num):
        temp = self.root
        maximumNumber = 0
        for i in range(31, -1, -1):
            bit = ((num >> i) & 1)
            if temp.children[1-bit]:
                maximumNumber = maximumNumber | (1<<i)
                temp = temp.children[1-bit]
            else:
                temp = temp.children[bit]
        return maximumNumber

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        trie = Trie()
        for num in nums:
            trie.insert(num)
        
        maxi = 0
        for num in nums:
            maxi = max(maxi, trie.getMax(num))
        return maxi
        
