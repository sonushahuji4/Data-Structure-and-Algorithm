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


# Space optimization

def frogJump(n, height):
    # Base case: If there's only one stair, no energy is needed
    if n == 1:
        return 0
    
    # Initialize the previous two results
    prev2 = 0  # dp[0], energy required to stay at the 0th stair
    prev1 = abs(height[1] - height[0])  # dp[1], energy to reach the 1st stair
    
    # Iterate from the 2nd stair to the (n-1)th stair
    for i in range(2, n):
        # Calculate the minimum energy to reach the i-th stair
        oneStep = prev1 + abs(height[i] - height[i-1])
        twoStep = prev2 + abs(height[i] - height[i-2])
        
        # Current energy required to reach i-th stair
        curr = min(oneStep, twoStep)
        
        # Update prev2 and prev1 for the next iteration
        prev2 = prev1
        prev1 = curr
    
    # Return the minimum energy required to reach the (n-1)th stair
    return prev1

# Example Usage:
n = 5
height = [10, 20, 30, 10, 40]
print(frogJump(n, height))  # Output: Minimum energy needed to reach the last stair

