# Link: https://leetcode.com/problems/find-k-closest-elements/description/

import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []
        for num in arr[:k]:
            heapq.heappush(minHeap,num)
        for num in arr[k:]:
            highestItem = abs(x - num)
            item = heapq.heappop(minHeap)
            lowestItem = abs(x - item)
            if lowestItem > highestItem:
                heapq.heappush(minHeap,num)
            else:
                heapq.heappush(minHeap,item)
        ans = [] 
        for i in range(len(minHeap)):
            item = heapq.heappop(minHeap)
            ans += [item]
        return ans
