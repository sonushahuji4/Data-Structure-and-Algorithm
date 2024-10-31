# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

from collections import defaultdict, deque

class DisjointSet:
    def __init__(self, n: int):
        self.parent = [node for node in range(n)]
        self.size = [1]*n
    
    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u: int, v: int):
        nodeU = self.find(u)
        nodeV = self.find(v)

        if nodeU == nodeV: return None

        if self.size[nodeU] < self.size[nodeV]:
            self.parent[nodeU] = nodeV
            self.size[nodeV] += self.size[nodeU]
        else:
            self.parent[nodeU] = nodeV
            self.size[nodeU] += self.size[nodeV]

class DFS:
    def __init__(self):
        pass
    
    def dfs(self, node: int, visited: List[bool], destination: int, graph: List[List[int]]) -> bool:
        visited[node] = True
        if node == destination:
            return True
        for neighbour in graph[node]:
            if not visited[neighbour]:
                if self.dfs(neighbour, visited, destination, graph):
                    return True
        return False
     
class BFS:
    def __init__(self):
        pass
    
    def bfs(slef, node: int, visited: List[bool], destination: int, graph: List[List[int]]) -> bool:
        visited[node] = True
        queue = deque()
        queue.append(node)

        while queue:
            currentNode = queue.popleft()
            if currentNode == destination: return True

            for neighbour in graph[currentNode]:
                if not visited[neighbour]:
                    visited[neighbour]= True
                    queue.append(neighbour)
        return False

class Solution:
    def buildGraph(self, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for source, destination in edges:
            graph[source].append(destination)
            graph[destination].append(source)
        return graph

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # Approach One
        # graph = self.buildGraph(edges)
        # visited = [False] * n
        # dfsInstance = DFS()
        # return dfsInstance.dfs(source, visited, destination, graph)

        # Approach Two
        graph = self.buildGraph(edges)
        visited = [False] * n
        bfsInstance = BFS()
        return bfsInstance.bfs(source, visited, destination, graph)

        # Approach Three
        # djs = DisjointSet(n)
        # for (u,v) in edges:
        #     djs.unionBySize(u,v)
        # if djs.find(source) == djs.find(destination): return True
        # return False

