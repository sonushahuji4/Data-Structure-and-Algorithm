# Given an array arr[] of size N and a number K, where K is smaller than the size of the array. 
# Find the K’th smallest element in the given array. Given that all array elements are distinct.

# Examples:  

# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3 
# Output: 7

# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4 
# Output: 10 

import heapq
class Solution:
    def findKthSmallest(self, nums: List[int], k: int) -> int:

        kthMaxHeap = []
        for num in nums[:k]:
            heapq.heappush(kthMaxHeap, -num)
        
        for num in nums[k:]:
            heapq.heappush(kthMaxHeap, -num)
            heapq.heappop(kthMaxHeap)

        kthElement = heapq.heappop(kthMaxHeap)
        return kthElement * -1
