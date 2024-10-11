# https://leetcode.com/problems/kth-missing-positive-number/description/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            missingNumber = arr[mid] - mid
            if missingNumber <= k:
                low = mid + 1
            else:
                high = mid - 1
        return high + k + 1
