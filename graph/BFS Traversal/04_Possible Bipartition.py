# https://leetcode.com/problems/possible-bipartition/description/

from collections import defaultdict, deque

class DisjointSet:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.size = [1]*n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        nodeU = self.find(u)
        nodeV = self.find(v)

        if nodeU == nodeV:
            return  # They are already in the same set

        if self.size[nodeU] < self.size[nodeV]:
            self.parent[nodeU] = nodeV
            self.size[nodeV] += self.size[nodeU]
        else:
            self.parent[nodeV] = nodeU
            self.size[nodeU] += self.size[nodeV]

class BFS:
    def __init__(self, n):
        self.visited = [-1]*n
    
    def bfs(self, node: int, graph: List[List[int]])-> bool:
        self.visited[node] = 1
        queue = deque()
        queue.append(node)

        while queue:
            currentNode = queue.popleft()
            for neighbour in graph[currentNode]:
                if self.visited[currentNode] == self.visited[neighbour]: 
                    return False
                if self.visited[neighbour] == -1:
                    self.visited[neighbour] = 1 - self.visited[currentNode]
                    queue.append(neighbour)
        return True


class Solution:

    def buildGraph(self,edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for (u,v) in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        # Approach One
        # dsu = DisjointSet(n+1)
        # graph = self.buildGraph(dislikes)

        # for node in range(1, n+1):
        #     for neighbour in graph[node]:
        #         if dsu.find(node) == dsu.find(neighbour): return False
        #         dsu.unionBySize(graph[node][0], neighbour)
        # return True

        # Approach Two
        graph = self.buildGraph(dislikes)
        bfsInstance = BFS(n+1)
        for node in range(1,n+1):
            if bfsInstance.visited[node] == -1:
                if not bfsInstance.bfs(node,graph): 
                    return False
        return True
