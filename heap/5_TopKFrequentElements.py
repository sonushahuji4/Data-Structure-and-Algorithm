# Link : https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencyMapper = defaultdict(int)
        for num in nums:
            frequencyMapper[num] += 1

        minHeap = []
        for key in frequencyMapper:
            item = (-frequencyMapper[key],key)
            minHeap += [item]
        heapq.heapify(minHeap)
        
        ans = []
        while k > 0:
            item = heapq.heappop(minHeap)
            frequency, num = item
            ans += [num]
            k -= 1
        return ans
