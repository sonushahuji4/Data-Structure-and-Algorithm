class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def getLowerBound(low, high, target):
            index = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] >= target:
                    index = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return index
        def getUpperBound(low, high, target):
            index = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    index = mid
                    low = mid + 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return index
        n = len(nums)
        ans1 = getLowerBound(0,n-1,target)
        ans2 = getUpperBound(0,n-1,target)
        if ans1 == -1 or ans2 == -1: return [-1,-1]
        return [ans1, ans2]

        
        
        
