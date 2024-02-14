# Link : https://leetcode.com/problems/k-closest-points-to-origin/description/

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        origin = [0,0]
        x1, y1 = origin
        distances = []
        for point in points:
            x2, y2 = point
            x = abs(x1-x2) 
            y = abs(y1-y2)
            distance = x*x + y*y
            distances += [(-distance,point)]
        
        minHeap = []
        for distance in distances[:k]:
            heapq.heappush(minHeap, distance)
        
        for distance in distances[k:]:
            heapq.heappush(minHeap, distance)
            heapq.heappop(minHeap)
  
        kClosedDistance = []
        while k > 0:
            distance, point = heapq.heappop(minHeap)
            kClosedDistance += [point]
            k -= 1

        return kClosedDistance
