# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def getTotalSum(divisor):
            totalSum = 0
            for num in nums:
                # The formula (num + divisor - 1) // divisor is a trick to divide two numbers and always round up to the next whole number, without using decimal points.
                totalSum += (num + divisor - 1) // divisor
            return totalSum
        
        n = len(nums)
        maxi = max(nums)

        low, high = 1, maxi
        while low <= high:
            mid = low + (high - low)//2
            totalSum = getTotalSum(mid)
            if totalSum <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low


        
