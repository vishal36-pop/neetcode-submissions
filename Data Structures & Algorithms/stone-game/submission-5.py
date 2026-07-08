class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[-1]*n for _ in range(n)]
        #base case i == j
        for i in range(n):
            dp[i][i] = piles[i]
        for j in range(1,n):
            for i in range(j-1,-1,-1):
                a = piles[i] - dp[i+1][j]
                b = piles[j] - dp[i][j-1]
                dp[i][j] = max(a,b)
        return dp[0][n-1] > 0