# Link: https://www.codingninjas.com/studio/problems/nearly-sorted_982937?leftPanelTabValue=PROBLEM

import heapq

def nearlySorted(arr, k):
    
    minHeap = []
    for num in arr[:k]:
        heapq.heappush(minHeap,num)
    
    ans = []
    for num in arr[k:]:
        heapq.heappush(minHeap,num)
        ans += [heapq.heappop(minHeap)]
    
    while k > 0:
        ans += [heapq.heappop(minHeap)]
        k -= 1
    return ans
