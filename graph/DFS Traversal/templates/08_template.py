# DFS with Counting (Counting Nodes, Subtree Sizes, etc.)
# Used to count nodes or accumulate specific values within a connected component or subtree.

class DFS:
    def __init__(self, n):
        self.count = 0  # Track count of nodes or accumulated value

    def dfs(self, node, graph):
        self.count += 1  # Increment count for each node visited
        self.visited[node] = True
        for neighbor in graph[node]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, graph)
