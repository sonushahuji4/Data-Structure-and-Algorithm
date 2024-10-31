class DFS:
    def __init__(self, n):
        self.visited = [False] * n
    
    def dfs(self, node, graph):
        self.visited[node] = True
        for neighbor in graph[node]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, graph)

class Solution:
    def countComponents(self, n, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dfsInstance = DFS(n)
        components = 0
        for i in range(n):
            if not dfsInstance.visited[i]:
                dfsInstance.dfs(i, graph)
                components += 1  # Increment for each connected component
        return components
