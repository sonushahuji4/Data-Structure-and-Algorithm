# When a graph problem involves finding a shortest path, BFS should be used over DFS.
def dfs(graph, node, visited):
    visited[node] = True
    print(node)  # Optional: Print or process the node

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# Example usage
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

# Number of nodes in the graph
n = len(graph)

# Initialize visited array
visited = [False] * n

# Perform DFS starting from node 0
dfs(graph, 0, visited)
