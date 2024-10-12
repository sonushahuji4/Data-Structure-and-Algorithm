# Recursion + DP
def frogJumpKSteps(n, height, k):
    # Initialize dp array where dp[i] will store the minimum energy to reach stair i
    dp = [-1] * n

    # Base case: If the frog is at the first stair, no energy is needed
    dp[0] = 0
    
    # Recursive function to calculate the minimum energy required to reach stair i
    def minEnergy(i):
        # If the value has already been computed, return it
        if dp[i] != -1: return dp[i]
        
        # Initialize the minimum energy required to a large value
        minEnergyRequired = float('inf')
        
        # Try all possible jumps from stair i-1, i-2, ..., i-k
        for j in range(1, k + 1):
            if i - j >= 0:  # Make sure we are within bounds
                jumpEnergy = minEnergy(i - j) + abs(height[i] - height[i - j])
                minEnergyRequired = min(minEnergyRequired, jumpEnergy)
        
        # Store the computed value in dp array and return it
        dp[i] = minEnergyRequired
        return dp[i]

    # Start the recursion from the last stair
    return minEnergy(n - 1)

# Example Usage:
n = 5
height = [10, 30, 40, 20, 50]
k = 3
print(frogJumpKSteps(n, height, k))  # Output: Minimum energy to reach the last stair


# Tabulation
def frogJumpKSteps(n, height, k):
    # Initialize dp array where dp[i] will store the minimum energy to reach stair i
    dp = [float('inf')] * n
    dp[0] = 0  # Base case: No energy required to stay at the first stair
    
    # Fill the dp table using tabulation
    for i in range(1, n):
        # Calculate the minimum energy to reach the i-th stair from the previous k stairs
        for j in range(1, k + 1):
            if i - j >= 0:  # Make sure we stay within bounds
                dp[i] = min(dp[i], dp[i - j] + abs(height[i] - height[i - j]))
    
    # The result will be the minimum energy to reach the last stair
    return dp[n - 1]

# Example Usage:
n = 5
height = [10, 30, 40, 20, 50]
k = 3
print(frogJumpKSteps(n, height, k))  # Output: Minimum energy to reach the last stair

