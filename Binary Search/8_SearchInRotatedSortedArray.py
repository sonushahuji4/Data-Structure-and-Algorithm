class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target: return mid
            if nums[low] <= nums[mid]: # right hand array sorted
                if nums[low] <= target <= nums[mid]: # check if target lies between (low and mid)
                    high = mid - 1
                else:
                    low = mid + 1
            else: # left hand array sorted
                if nums[mid] <= target <= nums[high]: # check if target lies between (high and mid)
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
        
