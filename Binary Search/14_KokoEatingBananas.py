# https://leetcode.com/problems/koko-eating-bananas/description/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def getTotalNumberOfHours(start, end):
            hours = 0
            for bananas in piles:
                hours += bananas//start
                if bananas % start != 0:
                    hours += 1
            return hours

        n = len(piles)
        low = 1
        high = max(piles)
        while low < high:
            mid = (low + high)//2
            totalHours = getTotalNumberOfHours(mid, high)
            if totalHours <= h:
                high = mid
            else:
                low = mid + 1
        return low
