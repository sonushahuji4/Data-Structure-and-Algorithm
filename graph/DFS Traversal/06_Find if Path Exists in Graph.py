# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

from collections import defaultdict

class Solution:
    def buildGraph(self, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for source, destination in edges:
            graph[source].append(destination)
            graph[destination].append(source)
        return graph
    
    def dfs(self, node: int, visited: List[bool], destination: int, graph: List[List[int]]) -> bool:
        visited[node] = True
        if node == destination:
            return True
        for neighbour in graph[node]:
            if not visited[neighbour]:
                if self.dfs(neighbour, visited, destination, graph):
                    return True
        return False
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.buildGraph(edges)
        visited = [False] * n
        return self.dfs(source, visited, destination, graph)
