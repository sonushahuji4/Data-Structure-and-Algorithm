class Solution:

    def getLowerBound(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        index = n
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                index = mid
                high = mid - 1
            else:
                low = mid + 1
        return index

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.getLowerBound(nums, target)
        
