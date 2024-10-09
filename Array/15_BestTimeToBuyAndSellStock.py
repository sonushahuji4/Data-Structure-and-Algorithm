# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxProfit = 0
        n = len(prices)
        for i in range(1,n):
            cost = prices[i] - mini
            maxProfit = max(maxProfit, cost)
            mini = min(mini, prices[i])
        return maxProfit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        sel = 0
        for i in range(1,n):
            # can i buy at cheaper rate ?
            if buy > prices[i]:
                buy = prices[i]
            if buy < prices[i]:
                sel = max(sel,prices[i] - buy)
            # how much profit do i make
        return sel



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        arr = [0]*n
        prevMax = prices[-1]
        i = n-1
        while i >= 0:
            arr[i] = max(prevMax, prices[i])
            prevMax = arr[i]
            i -= 1
        maxProfit = 0
        for i in range(n):
            maxProfit = max(maxProfit,arr[i] - prices[i])
     
        return maxProfit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        maxValueFromRight = [0]*n
        maxValueFromRight[-1] = prices[-1]
        i = n-2
        while i > -1:
            maxValueFromRight[i] = max(maxValueFromRight[i+1],prices[i])
            i -= 1

        for i in range(n):
            maxProfit = max(maxProfit,maxValueFromRight[i]-prices[i])
        return maxProfit
