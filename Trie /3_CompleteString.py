# Link : https://www.codingninjas.com/studio/problems/complete-string_2687860?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTabValue=PROBLEM

from sys import *
from collections import *
from math import *

from typing import *

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
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
        temp.isEndOfWord = True 
    
    def isPrefixPresent(self, word):
        temp = self.root
        for ch in word:
            charIndex = ord(ch) - ord('a')
            if temp.children[charIndex] == None: return False
            temp = temp.children[charIndex]
            if not temp.isEndOfWord: return temp.isEndOfWord
        return temp.isEndOfWord


def completeString(n: int, a: List[str]) -> str:
    trie = Trie()
    for i in range(n):
        trie.insert(a[i])
    
    longest = ""
    for i in range(n):
        if trie.isPrefixPresent(a[i]):
            if len(a[i]) > len(longest):
                longest = a[i]
            elif len(a[i]) == len(longest) and a[i] < longest:
                longest = a[i]
    if longest == "": return None
    return longest
