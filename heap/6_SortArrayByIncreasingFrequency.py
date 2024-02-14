from collections import defaultdict
import heapq

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        maxHeap = []
        for key in freq:
            heapq.heappush(maxHeap, (-freq[key], key))

        ans = []
        while maxHeap:
            freqCount, num = heapq.heappop(maxHeap)
            ans.extend([num] * (-1*freqCount))
        return ans[::-1]
