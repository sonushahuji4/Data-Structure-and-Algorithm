# https://leetcode.com/problems/all-paths-from-source-to-target/description/


# Variation One
from collections import defaultdict

class DFS:
    def __init__(self,n):
        self.visited = [False] * n
        self.n = n
    
    def dfs(self, node, destination, graph):
        if node == destination: return 1
        self.visited[node] = True
        pathCnt = 0
        for neighbour in graph[node]:
            if not self.visited[neighbour]:
                pathCnt += self.dfs(neighbour, destination, graph)
        self.visited[node] = False
        return pathCnt

class Solution:
    def buildGraph(self, edges, n):
        graph = defaultdict(list)
        for node in range(n):
            for neighbour in edges[node]:
                graph[node].append(neighbour)
        return graph

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        newGraph = self.buildGraph(graph,n)
        dfsInstance = DFS(n)
        cnt = dfsInstance.dfs(0, n-1, newGraph)
        return cnt


# Variation Two

from collections import defaultdict

class DFS:
    def __init__(self,n):
        self.visited = [False] * n
        self.n = n
        self.paths = []
    
    def dfs(self, node, destination, graph, path):
        if node == destination:
            self.paths.append(path)
            return
            
        self.visited[node] = True
       
        for neighbour in graph[node]:
            if not self.visited[neighbour]:
                self.dfs(neighbour, destination, graph, path + [neighbour])
                
        self.visited[node] = False
        

class Solution:
    def buildGraph(self, edges, n):
        graph = defaultdict(list)
        for node in range(n):
            for neighbour in edges[node]:
                graph[node].append(neighbour)
        return graph

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        newGraph = self.buildGraph(graph,n)
        dfsInstance = DFS(n)
        dfsInstance.dfs(0, n-1, newGraph, [0])
        return dfsInstance.paths
