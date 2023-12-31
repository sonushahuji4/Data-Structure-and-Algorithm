# Link : https://www.codingninjas.com/studio/problems/partitions-with-given-difference_3751628?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos

def countPartitions(n: int, d: int, arr: List[int]) -> int:
    MOD = 10**9 + 7
    total = sum(arr)
    n = len(arr)
    target = (total - d)//2
    dp = [[-1]*(target + 1) for _ in range(n)]

    def countSubsets(i, target, n):
        if target == 0:
            return 1

        if i == n or target < 0:  # Stop recursion if target becomes negative
            return 0
        if dp[i][target] != -1: return dp[i][target]

        cntLeft = 0
        if arr[i] <= target:
            cntLeft = countSubsets(i + 1, target - arr[i], n)
        cntRight = countSubsets(i + 1, target, n)
        
        dp[i][target] = (cntLeft + cntRight) % MOD
        return dp[i][target]

    return countSubsets(0, target, n)
