class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        dp = [[-1]*(amount + 1) for _ in range(n)]

        def solve(n, amount):
            if n == 0:
                if amount % coins[0] == 0: 
                    return (amount // coins[0])
                return int(1e9)

            if dp[n][amount] != -1: 
                return dp[n][amount]

            pick = int(1e9)
            if coins[n] <= amount:
                pick = 1 + solve(n, amount - coins[n])
            notPick = 0 + solve(n-1, amount)

            dp[n][amount] = min(pick,notPick)
            return dp[n][amount]

        ans = solve(n-1, amount)
        if ans >= int(1e9): return -1
        return ans
        
