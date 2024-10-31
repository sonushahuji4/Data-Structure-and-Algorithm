# Detects cycles in an undirected graph by checking if a visited node is revisited without being its direct parent.

class DFS:
    def __init__(self, n):
        self.visited = [False]*n
        self.n = n
    
    def dfs(self, node: int, parent: int, graph: List[List[int]]) -> bool:
        self.visited[node] = True # Mark the node as visited
        for neighbour in graph[node]:
            if neighbour == parent: # Skip the parent to avoid false positive
                continue
            if self.visited[neighbour]: # Cycle found
                return True
            if not self.visited[neighbour]: Recursively visit neighbours
                if self.dfs(neighbour, node, graph):
                    return True
        return False
        
class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        
        dfsInstance = DFS(V)
        for node in range(V):
            if not dfsInstance.visited[node] and dfsInstance.dfs(node, -1, adj): 
                return True
        return False
