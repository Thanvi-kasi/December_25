class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Create a 2D dp array to store the number of paths
        dp = [[0] * n for _ in range(m)]
        
        # If the starting point is not an obstacle, initialize it
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        
        # Fill the first column, can only come from above
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        # Fill the first row, can only come from the left
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
        # Fill the rest of the dp table
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The bottom-right corner will contain the result
        return dp[m-1][n-1]
