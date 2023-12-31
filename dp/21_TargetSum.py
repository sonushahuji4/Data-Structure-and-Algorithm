class Solution:
    def findTargetSumWays(self, nums, S):
        total = sum(nums)
        memo = [[float('-inf')] * (2 * total + 1) for _ in range(len(nums))]
        
        def calculate(i, curr_sum):
            if i == len(nums):
                return 1 if curr_sum == S else 0
            
            if memo[i][curr_sum + total] != float('-inf'):
                return memo[i][curr_sum + total]

            add = calculate(i + 1, curr_sum + nums[i])
            subtract = calculate(i + 1, curr_sum - nums[i])
            memo[i][curr_sum + total] = add + subtract
            return memo[i][curr_sum + total]

        return calculate(0, 0)
