class Solution:
    def findMin(self, nums: List[int]) -> int:
        minElement = 1000000007
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[low] <= nums[mid]:
                minElement = min(minElement, nums[low])
                low = mid + 1
            else:
                minElement = min(minElement, nums[mid])
                high = mid - 1
        return minElement
