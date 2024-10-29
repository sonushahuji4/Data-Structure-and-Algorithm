# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        
        # Helper function to perform DFS and detect cycle.
        def isCycleDFS(adj, node, visited, parent):
            # Mark the current node as visited
            visited[node] = True
            # Visit all the neighbors of the current node
            for neighbour in adj[node]:
                # Skip the parent node to avoid false cycle detection
                if neighbour == parent:
                    continue
                # If the neighbor is already visited and isn't the parent, a cycle is found
                if visited[neighbour]:
                    return True
                # Recursively check for cycles in the DFS path
                if not visited[neighbour] and isCycleDFS(adj, neighbour, visited, node):
                    return True
            # No cycle detected for the current path
            return False
        
        # Initialize a visited list to keep track of visited nodes
        visited = [False] * V
        # Iterate over each node in the graph
        for node in range(V):
            # If the node is not visited, perform DFS from that node
            if not visited[node] and isCycleDFS(adj, node, visited, -1):
                return True
        # No cycle found in any component of the graph
        return False
