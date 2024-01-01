# Link : https://leetcode.com/problems/maximum-length-of-repeated-subarray/submissions/1133364232/

# Longest Common Substring on Numbers

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        dp = [[0]*(m + 1) for _ in range(n+1)]
        maxSubString = 0
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    maxSubString = max(maxSubString, dp[i][j])
                else:
                    dp[i][j] = 0
        return maxSubString


# Link : https://www.codingninjas.com/studio/problems/longest-common-substring_1235207?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION
# Longest Common Substring on String

def lcs(str1: str, str2: str) -> int:
    n = len(str1)
    m = len(str2)

    dp = [[0]*(m + 1) for _ in range(n+1)]
    maxSubString = 0
    for i in range(n):
        for j in range(m):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
                maxSubString = max(maxSubString, dp[i][j])
            else:
                dp[i][j] = 0
    return maxSubString
