class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high + low) // 2

            if nums[mid] == target: return True
            if nums[low] == nums[mid] and nums[mid] == nums[high]: # Shrink from left and from right
                low = low + 1
                high = high - 1
                continue

            if nums[low] <= nums[mid]: # right hand array sorted
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else: # left hand array sorted
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
        
        
