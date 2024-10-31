# When to Use It

# Use this template anytime you need to count or identify clusters in graphs, grids, or datasets where connectivity defines grouping 
# (e.g., islands, friend circles, network segments).
# This makes it highly versatile for both graph and grid problems that involve grouping or connectivity constraints.


# Core Idea in Practice

# This logic works well for clustering problems because DFS naturally partitions nodes into groups based on reachability:
# Nodes reachable from the same starting point belong to the same component.
# Nodes unreachable from each other belong to separate components.
# This concept can extend beyond graphs to any data structure or problem where connectivity, reachability, or grouping is involved.


class DFS:
    def __init__(self, n):
        self.visited = [False] * n
        self.n = n
    
    def dfs(self, node: int, graph: List[List[int]]):
        self.visited[node] = True  # Mark as visited
        for neighbour in range(self.n):  # Iterate neighbors
            if not self.visited[neighbour] and graph[node][neighbour]:  # Corrected check
                self.dfs(neighbour, graph)  # Recursive call

class Solution:
    def countComponents(self, n, edges):
        dfsInstance = DFS(n)
        components = 0
        for node in range(n):
            if not dfsInstance.visited[node]:
                dfsInstance.dfs(node, graph)
                components += 1  # Increment for each connected component
        return components
