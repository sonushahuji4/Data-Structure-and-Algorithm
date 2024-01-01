
class Solution:
    def fib(self, n: int) -> int:

      # Recursion
      def fibo(n):
        if n == 1: return 1
        if n == 0: return 0
        leftCnt = fibo(n-1)
        rightCnt = fibo(n-2)
        return leftCnt + rightCnt
      return fibo(n)

      # Recursion + dp
      dp = [-1]*(n+1)
      def fibo(n):
        if n == 1: return 1
        if n == 0: return 0
        if dp[n] != -1: return dp[n]

        leftCnt = fibo(n-1)
        rightCnt = fibo(n-2)
        
        dp[n] = leftCnt + rightCnt
        return dp[n]
      return fibo(n)
