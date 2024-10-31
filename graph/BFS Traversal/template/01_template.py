class BFS:
    def __init__(self):
        pass
    
    def bfs(slef, node: int, visited: List[bool], destination: int, graph: List[List[int]]) -> bool:
        visited[node] = True
        queue = deque()
        queue.append(node)

        while queue:
            currentNode = queue.popleft()
            if currentNode == destination: return True

            for neighbour in graph[currentNode]:
                if not visited[neighbour]:
                    visited[neighbour]= True
                    queue.append(neighbour)
        return False

class Solution:
    def buildGraph(self, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for source, destination in edges:
            graph[source].append(destination)
            graph[destination].append(source)
        return graph

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # Approach Two
        graph = self.buildGraph(edges)
        visited = [False] * n
        bfsInstance = BFS()
        return bfsInstance.bfs(source, visited, destination, graph)
