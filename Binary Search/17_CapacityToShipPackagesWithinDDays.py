# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        n = len(weights)

        def findDays(capacity):
            load = 0
            day = 1
            for i in range(n):
                if load + weights[i] > capacity:
                    day += 1
                    load = weights[i]
                else:
                    load += weights[i]
            return day

        def findLeastWeightCapacity():
            low = max(weights)
            high = sum(weights)
            while low <= high:
                mid = (high + low)//2
                numberOfDays = findDays(mid)
                if numberOfDays <= days:
                    high = mid - 1
                else:
                    low = mid + 1
            return low
        return findLeastWeightCapacity()
