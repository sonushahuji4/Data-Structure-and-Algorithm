# https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-weighted-undirected-graph


#User function Template for python3
from typing import List
from collections import defaultdict
import heapq
class Solution:
    
    def addEdges(self, edges: List[List[int]]) -> defaultdict:
        graph = defaultdict(list)
        for source, destination, weight in edges:
            graph[source].append((destination, weight))
            graph[destination].append((source, weight))
        return graph
    
    def dijkstraAlgo(self, graph, start, n):
        distances = {node: float('inf') for node in range(1, n + 1)}
        distances[start] = 0
        minHeapQ = [(0, start)]
        predecessors = {node: None for node in range(1, n + 1)}
        
        while minHeapQ:
            currentDistance, currentNode = heapq.heappop(minHeapQ)
            
            if currentDistance > distances[currentNode]:
                continue
            
            for neighbor, weight in graph[currentNode]:
                distance = weight + currentDistance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = currentNode
                    heapq.heappush(minHeapQ, (distance, neighbor))
                
        return distances, predecessors
        
    def reconstructPath(self, predecessors, target):
        path = []
        while target is not None:
            path.append(target)
            target = predecessors[target]
        path.reverse()
        return path
        
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> int:
        graph = self.addEdges(edges)
        distances, predecessors = self.dijkstraAlgo(graph, 1, n)
        if distances[n] == float('inf'): return [-1]
        path = self.reconstructPath(predecessors, n)
        return [distances[n]] + path
        
        
        


#{ 
 # Driver Code Starts
from collections import defaultdict


def check(n, path, edges):
    gp = [{} for i in range(n + 1)]
    for u, v, w in edges:
        if v in gp[u]:
            gp[u][v] = min(gp[u][v], w)
        else:
            gp[u][v] = w

        if u in gp[v]:
            gp[v][u] = min(gp[v][u], w)
        else:
            gp[v][u] = w

    s = 0
    for i in range(2, len(path)):
        if path[i] not in gp[path[i - 1]]:
            return False
        s += gp[path[i - 1]][path[i]]

    return s == path[0]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        edges = []
        for i in range(m):
            a, b, w = map(int, input().split())
            edges.append([a, b, w])

        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        if res[0] == -1:
            print(-1)
        else:
            if check(n, res, edges):
                print(res[0])
            else:
                print(-2)
        print("~")

# } Driver Code Ends
