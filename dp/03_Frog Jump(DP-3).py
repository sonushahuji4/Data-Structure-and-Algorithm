# Problem Statement:

# Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. 
# At a time the frog can climb either one or two steps. A height[N] array is also given. 
# Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.

# Recursion + DP
def frogJump(n, height):
    # Create a dp array initialized with -1 (which means uncalculated state)
    dp = [-1] * n
    
    # Helper function for recursion + memoization
    def minEnergy(i):
        # Base case: If the frog is on the 0th stair, no energy is needed
        if i == 0: return 0
        
        # If dp[i] is already calculated, return it
        if dp[i] != -1: return dp[i]
        
        # Calculate the minimum energy required to reach i-th stair
        # Option 1: Coming from (i-1)th stair
        oneStep = minEnergy(i-1) + abs(height[i] - height[i-1])
        
        # Option 2: Coming from (i-2)th stair (if i > 1)
        twoStep = float('inf')
        if i > 1:
            twoStep = minEnergy(i-2) + abs(height[i] - height[i-2])
        
        # Memoize the result (store the minimum energy for reaching i-th stair)
        dp[i] = min(oneStep, twoStep)
        
        return dp[i]
    
    # The minimum energy to reach the last stair (n-1)
    return minEnergy(n-1)

# Example Usage:
n = 5
height = [10, 20, 30, 10, 40]
print(frogJump(n, height))  # Output: Minimum energy needed to reach the last stair


# Tabulation

def frogJump(n, height):
    # Base case
    if n == 1:
        return 0

    # Initialize dp array where dp[i] represents the minimum energy to reach i-th stair
    dp = [0] * n
    dp[0] = 0  # No energy needed to be on the first stair

    for i in range(1, n):
        # Calculate the energy for a one-step jump
        one_step = dp[i-1] + abs(height[i] - height[i-1])
        
        # Calculate the energy for a two-step jump if possible
        two_step = float('inf')
        if i > 1:
            two_step = dp[i-2] + abs(height[i] - height[i-2])
        
        # Take the minimum of the one-step or two-step energy cost
        dp[i] = min(one_step, two_step)

    # The minimum energy to reach the last stair
    return dp[n-1]

# Example Usage:
n = 5
height = [10, 20, 30, 10, 40]
print(frogJump(n, height))  # Output will be the minimum energy needed
