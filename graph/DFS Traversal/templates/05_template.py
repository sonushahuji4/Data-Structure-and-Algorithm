# DFS for Topological Sort (Directed Acyclic Graph)
# Performs a post-order DFS to get topological ordering.

class DFS:
    def __init__(self, n):
        self.visited = [False] * n
        self.stack = []  # Stores nodes in topological order
    
    def dfs(self, node, graph):
        self.visited[node] = True
        for neighbor in graph[node]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, graph)
        self.stack.append(node)  # Append after all neighbors are visited

class Solution:
    def topologicalSort(self, n, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        dfsInstance = DFS(n)
        for i in range(n):
            if not dfsInstance.visited[i]:
                dfsInstance.dfs(i, graph)

        return dfsInstance.stack[::-1]  # Return reversed stack for topological order
