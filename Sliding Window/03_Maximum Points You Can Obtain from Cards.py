# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)
        maxSum = lSum = sum(cardPoints[:k])
        rSum = 0
        low, high = k - 1, size - 1
        while low >= 0:
            lSum -= cardPoints[low]
            rSum += cardPoints[high]
            high -= 1
            low  -= 1
            maxSum = max(maxSum, lSum + rSum)
        return maxSum
