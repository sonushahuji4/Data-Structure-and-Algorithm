class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(low,high):
            if low > high: return -1
            mid = low + (high - low)//2
            if nums[mid] == target: return mid
            elif target > nums[mid]:
                return binarySearch(mid + 1, high)
            else:
                return binarySearch(low, mid - 1)
                
        return binarySearch(0, len(nums)-1)
            

        
