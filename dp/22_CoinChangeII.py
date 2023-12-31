# Link : https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        dp = [[-1]*(amount + 1) for _ in range(n)]

        def solve(i,total):
            if i == n:
                if total == amount: return 1
                return 0

            if i > n or total > amount: return 0

            if dp[i][total] != -1: return dp[i][total]
            
            pick = solve(i, total + coins[i])
            notPick = solve(i+1, total)

            dp[i][total] = pick + notPick
            return dp[i][total]

        return solve(0,0)
        
