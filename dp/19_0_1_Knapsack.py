# Link : https://www.codingninjas.com/studio/problems/0-1-knapsack_920542?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

from os import *
from sys import *
from collections import *
from math import *

for _ in range(int(input())):
    n = int(input())
    weights = list(map(int, input().split()))
    values = list(map(int, input().split()))
    weightLimit = int(input())
    
    dp = [[-1] * (weightLimit + 1) for _ in range(n + 1)]
    
    def solve(n, w):
        if n == 0:
            if weights[0] <= w: 
                return values[0]
            return 0

        if dp[n][w] != -1: 
            return dp[n][w]

        pick = -float('inf')
        if weights[n] <= w:
            pick = values[n] + solve(n - 1, w - weights[n])
        
        notPick = 0 + solve(n - 1, w)
        dp[n][w] = max(pick, notPick)
        return dp[n][w]

    result = solve(n - 1, weightLimit)
    print(result)
