# DFS with Memoization (Dynamic Programming on Trees)
# Memoizes the results of subproblems for trees, often useful for calculating the sum of subtree values or path lengths.

class DFS:
    def __init__(self, n):
        self.memo = [-1] * n  # Store results for each node

    def dfs(self, node, parent, graph):
        if self.memo[node] != -1:
            return self.memo[node]  # Return cached result if available

        result = 1  # Example calculation, may vary with problem requirements
        for neighbor in graph[node]:
            if neighbor != parent:
                result += self.dfs(neighbor, node, graph)

        self.memo[node] = result  # Cache result for node
        return result
