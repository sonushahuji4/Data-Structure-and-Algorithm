# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        def isPossibleToFormMbouquests(days):
            count = 0
            ans = 0
            for i in range(n):
                if bloomDay[i] <= days:
                    count += 1
                else:
                    ans += count//k
                    count = 0
            ans += count//k
            return ans >= m
        
        val = m * k
        if val > n:
            return -1
        
        mini = float('inf')
        maxi = float('-inf')
        for i in range(n):
            mini = min(mini, bloomDay[i])
            maxi = max(maxi, bloomDay[i])

        low = mini
        high = maxi
        while low <= high:
            mid = (low + high) // 2
            if isPossibleToFormMbouquests(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
