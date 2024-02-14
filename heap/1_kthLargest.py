# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# 1. heapq.heappush(heap, item) -> Push the value item onto the heap, maintaining the heap invariant.
# 2. heapq.heappop(heap), -> Pop and return the smallest item from the heap,
# 3. heapq.heapify(x) -> Transform list x into a heap, in-place, in linear time.
# Link : https://www.youtube.com/watch?v=4BfL2Hjvh8g&list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9&index=2
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        kthMinHeap = []
        for num in nums[:k]:
            heapq.heappush(kthMinHeap, num)
        
        for num in nums[k:]:
            heapq.heappush(kthMinHeap, num)
            heapq.heappop(kthMinHeap)

        kthElement = heapq.heappop(kthMinHeap)
        return kthElement
