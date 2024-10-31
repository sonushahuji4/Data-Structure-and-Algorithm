# 1. Basic DFS Traversal
# A straightforward traversal template, useful for visiting nodes or marking them as visited.
class DFS:
    def __init__(self, n):
        self.visited = [False] * n
    
    def dfs(self, node, graph):
        self.visited[node] = True  # Mark the node as visited
        for neighbor in graph[node]:  # Explore neighbors
            if not self.visited[neighbor]:
                self.dfs(neighbor, graph)  # Recursive call for unvisited neighbors
