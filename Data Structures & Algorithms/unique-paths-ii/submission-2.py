class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #the dp shape is m*n 
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        #base case 
        dp[m-1][n-1] = 1 if obstacleGrid[m-1][n-1] == 0 else 0
        #i,j depends i+1,j i,j+1
        for j in range(n-1,-1,-1):
            for i in range(m-1,-1,-1):
                if not obstacleGrid[i][j]:
                    if i != m-1 and j != n-1 :
                        dp[i][j] = (dp[i+1][j] if obstacleGrid[i+1][j] != 1 else 0) + (dp[i][j+1] if not obstacleGrid[i][j+1] else 0)
                    elif i != m-1 and j == n-1:
                        dp[i][j] = dp[i+1][j] if obstacleGrid[i+1][j] != 1 else 0
                    elif i == m-1 and j != n-1:
                        dp[i][j] = dp[i][j+1] if obstacleGrid[i][j+1] != 1 else 0
        return dp[0][0]
