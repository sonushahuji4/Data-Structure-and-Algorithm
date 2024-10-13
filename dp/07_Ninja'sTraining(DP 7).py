# https://www.geeksforgeeks.org/problems/geeks-training/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=geeks-training

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


# Driver code starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())  # Number of days
        arr = [list(map(int, input().split())) for _ in range(n)]  # Points array
        ob = Solution()
        print(ob.maximumPoints(arr, n))
