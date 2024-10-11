# Link : https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:

      # Recursion
      def ways(n):
        if n == 0 or n == 1: return 1
        if n < 0: return 0
        leftWays = ways(n-1)
        rightWays = ways(n-2)
        return leftWays + rightWays
        
      return ways(n)

      # Recursion + dp
      dp = [-1] * (n+1)
      def ways(n):
        if n == 0 or n == 1: return 1
        if n < 0: return 0
        if dp[n] != -1: return dp[n]
        leftWays = ways(n-1)
        rightWays = ways(n-2)
        dp[n] = leftWays + rightWays
        return dp[n]
        
      return ways(n)
