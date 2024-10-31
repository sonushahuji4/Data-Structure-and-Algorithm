# https://leetcode.com/problems/keys-and-rooms/description/

from collections import defaultdict, deque

class DFS:
    def __init__(self, n: int):
        self.visited = [False]*n
    
    def dfs(self, node: int, graph: List[List[int]]) -> List[int]:
        self.visited[node] = True

        for neighbour in graph[node]:
            if not self.visited[neighbour]:
                self.dfs(neighbour, graph)

        return self.visited

class BFS:
    def __init__(self, n: int):
        self.visited = [False]*n

    def bfs(self, node: int, graph: List[List[int]]) -> List[int]:
        self.visited[node] = True
        queue = deque()
        queue.append(node)

        while queue:
            currentNode = queue.popleft()
            for neighbour in graph[currentNode]:
                if not self.visited[neighbour]:
                    self.visited[neighbour] = True
                    queue.append(neighbour)

        return self.visited

class Solution:

    def buildGraph(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for node in range(n):
            for neighbour in edges[node]:
                graph[node].append(neighbour)
        return graph

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        roomsLength = len(rooms)
        graph = self.buildGraph(roomsLength, rooms)

        # Approach One
        # dfsInstance = DFS(roomsLength)
        # visited = dfsInstance.dfs(0, graph)
        # for isVisited in visited:
        #     if not isVisited: return False
        # return True

        # Approach Two

        bfsInstance = BFS(roomsLength)
        visited = bfsInstance.bfs(0, graph)
        for isVisited in visited:
            if not isVisited: return False
        return True
