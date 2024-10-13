# https://www.geeksforgeeks.org/problems/geeks-training/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=geeks-training

# Recursion + DP
class Solution:
    def maximumPoints(self, points, n):
        # Recursive function to calculate maximum points with memoization
        def maximum(day, last, points, dp):
            if dp[day][last] != -1:  # Return cached result if already calculated
                return dp[day][last]
            
            if day == 0:
                # On the first day, pick the best activity not equal to `last`
                maxi = 0
                for task in range(3):
                    if task != last:
                        maxi = max(maxi, points[0][task])
                dp[day][last] = maxi
                return maxi
            
            maxi = 0
            # Try all activities except `last` and pick the one that maximizes points
            for task in range(3):
                if task != last:
                    point = points[day][task] + maximum(day - 1, task, points, dp)
                    maxi = max(maxi, point)
            
            dp[day][last] = maxi  # Store result in dp array
            return dp[day][last]
        
        # dp table initialized to -1
        dp = [[-1 for _ in range(4)] for _ in range(n)]
        # Start the recursion from the last day with no previous activity (i.e., last = 3)
        return maximum(n - 1, 3, points, dp)


# Tabulation

def maximumPoints(self, points, n):
    # dp array to store the maximum points up to each day for each activity
    dp = [[0] * 3 for _ in range(n)]
    
    # Base case for day 0
    dp[0][0] = points[0][0]  # Running on day 0
    dp[0][1] = points[0][1]  # Fighting on day 0
    dp[0][2] = points[0][2]  # Learning Practice on day 0
    
    # Fill the dp table iteratively for each day
    for day in range(1, n):
        # If Geek performs Running today, he can either come from Fighting or Learning Practice from the previous day
        dp[day][0] = points[day][0] + max(dp[day - 1][1], dp[day - 1][2])
        
        # If Geek performs Fighting today, he can either come from Running or Learning Practice from the previous day
        dp[day][1] = points[day][1] + max(dp[day - 1][0], dp[day - 1][2])
        
        # If Geek performs Learning Practice today, he can either come from Running or Fighting from the previous day
        dp[day][2] = points[day][2] + max(dp[day - 1][0], dp[day - 1][1])
    
    # The result is the maximum points Geek can have on the last day with any of the three activities
    return max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])
