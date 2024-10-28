# https://leetcode.com/problems/alien-dictionary/description/


from collections import defaultdict, deque
from typing import List

class KahnsTopgSortAlgo:
    def __init__(self, unique_chars, edges):
        self.graph = defaultdict(list)
        self.inDegree = {char: 0 for char in unique_chars}  # initialize inDegree for each unique character
        
        self.buildGraph(edges)
        self.initializeQueue()
    
    def buildGraph(self, edges):
        # Create the adjacency list and populate in-degrees
        for (source, destination) in edges:
            self.graph[source].append(destination)
            self.inDegree[destination] += 1
    
    def initializeQueue(self):
        # Initialize queue with nodes having 0 in-degree
        self.queue = deque([node for node in self.inDegree if self.inDegree[node] == 0])
    
    def topoSort(self):
        topoSort = []
        while self.queue:
            node = self.queue.popleft()
            topoSort.append(node)
            for neighbor in self.graph[node]:
                self.inDegree[neighbor] -= 1
                if self.inDegree[neighbor] == 0:
                    self.queue.append(neighbor)
        
        # If topoSort length matches the unique characters, return order
        if len(topoSort) == len(self.inDegree):
            return "".join(topoSort)
        return ""  # Cycle detected or incomplete sort


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Gather all unique characters
        unique_chars = set(char for word in words for char in word)
        
        # Step 2: Build edges based on lexical order
        edges = []
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLength = min(len(word1), len(word2))
            
            # Check if word1 is a prefix of word2 (invalid case)
            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return ""
            
            # Find the first differing character
            for j in range(minLength):
                if word1[j] != word2[j]:
                    edges.append((word1[j], word2[j]))
                    break
        
        # Step 3: Apply Kahn's Topological Sort
        ktsl = KahnsTopgSortAlgo(unique_chars, edges)
        return ktsl.topoSort()
