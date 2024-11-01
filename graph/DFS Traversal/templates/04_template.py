# DFS for Path Finding (Backtracking)
# Used to find all paths from a starting node to a target node in a graph, storing paths as they are discovered.

# 1. Variation One

class DFS:
    def __init__(self, n):
        self.visited = [False] * n
        self.paths = []  # Store all paths found
    
    def dfs(self, node, target, graph, path):
        path.append(node)  # Add node to path
        if node == target:
            self.paths.append(list(path))  # Add a copy of the path to paths
        else:
            for neighbor in graph[node]:
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    self.dfs(neighbor, target, graph, path)
                    self.visited[neighbor] = False  # Backtrack
        path.pop()  # Remove node from path on backtracking
      

# 2. Variation Two

class DFS:
    def __init__(self, n):
        self.visited = [False]*n
    
    def dfs(self, node: int, destination: int, graph: List[List[int]]) -> bool:
        self.visited[node] = True
        if node == destination:
            return True
        for neighbour in graph[node]:
            if not self.visited[neighbour]:
                if self.dfs(neighbour, destination, graph):
                    return True
        return False


# 3. Variation Three

class DFS:
    def __init__(self,n):
        self.visited = [False] * n
        self.n = n
        self.paths = []
    
    def dfs(self, node, destination, graph, path):
        if node == destination:
            self.paths.append(path)
            return
            
        self.visited[node] = True
       
        for neighbour in graph[node]:
            if not self.visited[neighbour]:
                self.dfs(neighbour, destination, graph, path + [neighbour])
                
        self.visited[node] = False
     
