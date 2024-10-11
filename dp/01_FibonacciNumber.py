# Link : https://leetcode.com/problems/fibonacci-number/

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


    # Tabulation
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]


    # Space optimization
    previous2 = 0
    previous1 = 1
    for i in range(2,n+1):
        current = previous1 + previous2
        previous2 = previous1
        previous1 = current
    return previous1
        
        
