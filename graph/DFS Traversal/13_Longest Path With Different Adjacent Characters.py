
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

from collections import defaultdict

class DFS:
    def __init__(self,n):
        self.result = 0
    
    def dfs(self, node, parent, labels, graph):
       
        longestChain = secondLongestChain = 0
        for neighbour in graph[node]:
            if neighbour == parent: continue
            childPathLength = self.dfs(neighbour, node, labels, graph)
            if labels[neighbour] == labels[node]: continue
            secondLongestChain = max(secondLongestChain,childPathLength)
            if secondLongestChain > longestChain:
                longestChain, secondLongestChain = secondLongestChain, longestChain


        pathThroughNode = 1 + longestChain + secondLongestChain
       
        self.result = max(self.result, pathThroughNode)
        return 1 + longestChain
        
        

class Solution:
    def buildGraph(self, edges, n):
        graph = defaultdict(list)
        for node in range(n):
            neighbour = edges[node]
            if neighbour == -1: continue
            graph[node].append(neighbour)
            graph[neighbour].append(node)

        return graph

    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        dfsInstance = DFS(n)
        graph = self.buildGraph(parent, n)
        dfsInstance.dfs(0,-1, s, graph)
        return dfsInstance.result
       
