# DFS with Depth Tracking (e.g., for Tree Problems)
# Tracks depth as it traverses, useful for calculating tree depths, heights, or distances.

class DFS:
    def __init__(self, n):
        self.depths = [-1] * n  # Store depth of each node

    def dfs(self, node, parent, depth, graph):
        self.depths[node] = depth  # Set depth of current node
        for neighbor in graph[node]:
            if neighbor != parent:
                self.dfs(neighbor, node, depth + 1, graph)  # Increment depth for children
