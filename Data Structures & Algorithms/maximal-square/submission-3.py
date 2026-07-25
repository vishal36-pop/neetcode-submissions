class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        #basecase 
        #if i or j goes out bound its 0
        for i in range(m+1):
            dp[i][n] = 0
        for j in range(n+1):
            dp[m][j] = 0
        ans = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                    continue
                dp[i][j] = 1 + min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
                ans = max(ans,dp[i][j]**2)
        return ans