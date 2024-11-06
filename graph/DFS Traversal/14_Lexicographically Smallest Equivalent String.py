# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/

from collections import defaultdict

class DFS:
    def __init__(self, numNodes):
        self.visited = set()

    def dfs(self, currentNode, graph):
        # Mark the current node as visited to prevent cycles
        self.visited.add(currentNode)
        
        # Start with the character value of the current node
        minCharValue = ord(currentNode)
        
        for neighbor in graph[currentNode]:
            # Skip the parent and already visited nodes
            if neighbor in self.visited:
                continue
            
            # Perform DFS on the neighbor to find the smallest character in its subtree
            neighborMinCharValue = self.dfs(neighbor, graph)
            minCharValue = min(minCharValue, neighborMinCharValue)
        
        return minCharValue

class Solution:
    def buildGraph(self, str1, str2, numNodes):
        graph = defaultdict(list)
        for i in range(numNodes):
            char1 = str1[i]
            char2 = str2[i]
            graph[char1].append(char2)
            graph[char2].append(char1)
        return graph

    def smallestEquivalentString(self, str1: str, str2: str, baseString: str) -> str:
        numNodes = len(str1)
        graph = self.buildGraph(str1, str2, numNodes)
        
        # Initialize DFS instance
        dfsInstance = DFS(numNodes)
        
        resultString = ""
        for i in range(len(baseString)):
            # Clear visited nodes for each new DFS call
            dfsInstance.visited.clear()
            
            # Find the smallest character equivalent for the current baseString character
            smallestCharValue = dfsInstance.dfs(baseString[i], graph)
            resultString += chr(smallestCharValue)
        
        return resultString
