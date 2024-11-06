# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/

from collections import defaultdict
import sys

class Solution:
    def buildGraph(self, n: int, edges: List[int]) -> List[int]:
        graph = defaultdict(list)
        for node in range(n):
            if edges[node] == -1: continue
            graph[node].append(edges[node])
        return graph

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        INT_MAX = sys.maxsize
        graph = self.buildGraph(n, edges)
        visitedOne = [False]*n
        visitedTwo = [False]*n
        distanceOne = [INT_MAX]*n
        distanceTwo = [INT_MAX]*n
        distanceOne[node1] = 0
        distanceTwo[node2] = 0

        def dfs(node, graph, visited, distance):
            visited[node] = True
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    distance[neighbour] = 1 + distance[node]
                    dfs(neighbour, graph, visited, distance)
            
        
        dfs(node1, graph, visitedOne, distanceOne)
        dfs(node2, graph, visitedTwo, distanceTwo)

        minDistanceNode = -1
        minDistanceTillNow = INT_MAX
        for index in range(n):
            maxD = max(distanceOne[index], distanceTwo[index])
            if minDistanceTillNow > maxD:
                minDistanceTillNow = maxD
                minDistanceNode = index
        return minDistanceNode
