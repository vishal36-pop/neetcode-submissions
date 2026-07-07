class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[0]*len(piles) for _ in range(len(piles))]
        n = len(piles)
        print(n)
        for i in range(n):
            dp[i][i] = float('inf')
        for j in range(1,n):
            for i in range(j,-1,-1):
                if abs(i-j) == 1 :
                    dp[i][j] = max(piles[i],piles[j])
                    continue
                #take i
                dp[i][j] = max(dp[i][j],piles[i]+min(dp[i+2][j] if i+2 < n else float('inf'),dp[i+1][j-1] if i+1 < n and j-1 >=0 else float('inf')))
                #take j
                dp[i][j] = max(dp[i][j],piles[j]+min(dp[i+1][j-1] if i+1 < n and j-1 >=0 else float('inf') ,dp[i][j-2] if j-2 >= 0 else float('inf')))
        return dp[0][len(piles)-1] > sum(piles)//2