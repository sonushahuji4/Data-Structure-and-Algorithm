class Solution:
    def fib(self, n: int) -> int:

        1. Recursion + DP Approach
        dp = [-1]*(n+1)
        def fib(n):
           if n <=1: return n
           if dp[n] != -1: return dp[n]
           dp[n] = fib(n-1) + fib(n-2)
           return dp[n]
        return fib(n)

        2. Tabulaton (Time complexity optimized)
        if n == 0: return 0
        dp = [-1]*(n+1)
        dp[0], dp[1] = 0, 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

        # 3. Tabulaton (Time complexity optimized and space complexity optimized)
        if n == 0: return n
        prev2 = 0
        prev1 = 1
        for i in range(2,n+1):
            cur_i = prev1 + prev2
            prev2 = prev1
            prev1 = cur_i
        return prev1
