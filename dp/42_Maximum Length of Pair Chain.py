class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        # Approach One (Recursion)
        def getLongestChain(ind, prev, n, pairs):
            if ind == n: return 0

            pick = 0
            if prev == -1 or pairs[ind][0] > pairs[prev][1]:
                pick = 1 + getLongestChain(ind+1, ind, n, pairs)
            
            notPick = 0 + getLongestChain(ind+1, prev, n, pairs)

            return max(pick, notPick)
        
        pairs.sort(key = lambda x: x[1])
        return getLongestChain(0,-1,len(pairs), pairs)

        # Approach Two (Recursion + Dp)
        n = len(pairs)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        def getLongestChain(ind, prev, n, pairs):
            if ind == n: return 0

            if dp[ind][prev] != -1: return dp[ind][prev]

            pick = 0
            if prev == -1 or pairs[ind][0] > pairs[prev][1]:
                pick = 1 + getLongestChain(ind+1, ind, n, pairs)
            
            notPick = 0 + getLongestChain(ind+1, prev, n, pairs)

            dp[ind][prev] = max(pick, notPick)
            return dp[ind][prev]
        
        pairs.sort(key = lambda x: x[1])
        return getLongestChain(0,-1, n, pairs)

        # Approach Three (Tabulation)
        n = len(pairs)
        pairs.sort(key = lambda x: x[1])
        dp = [1]*(n+1)
        for ind in range(1, n):
            for prev in range(ind):
                if pairs[ind][0] > pairs[prev][1]:
                    dp[ind] = max(dp[ind], dp[prev] + 1)
        return max(dp)
