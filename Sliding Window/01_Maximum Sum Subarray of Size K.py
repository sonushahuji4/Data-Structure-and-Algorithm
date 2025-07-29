# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/maximum-sum-subarray-of-size-k-easy

class Solution:
  def maxSumSubarray(self, nums: List[int], k: int) -> int:
    size = len(nums)
    maxSum = windowSum = left = 0
    for right in range(size):
      windowSum += nums[right]
      if right - left + 1 == k:
        maxSum = max(maxSum, windowSum)
        windowSum -= nums[left]
        left += 1
    return maxSum
