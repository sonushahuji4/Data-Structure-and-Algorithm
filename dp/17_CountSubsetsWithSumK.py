# Link : https://www.codingninjas.com/studio/problems/count-subsets-with-sum-k_3952532?leftPanelTabValue=PROBLEM

from typing import List

def findWays(arr: List[int], target: int) -> int:
    
    MOD = 10**9 + 7
    n = len(arr)
    dp = [[0]*(target + 1) for _ in range(n)]

    def countsSubset(i, target):
        if target == 0:
            return 1
        if i == n:
            if target == 0: return 1
            return 0
          
        if dp[i][target] != 0:
            return dp[i][target]

        # Include the current element in the sum
        cntLeft = 0
        if arr[i] <= target:
            cntLeft = countsSubset(i + 1, target - arr[i])

        # Exclude the current element from the sum
        cntRight = countsSubset(i + 1, target)

        dp[i][target] = (cntLeft + cntRight) % MOD
        return dp[i][target]

    return countsSubset(0, target) % MOD
 
