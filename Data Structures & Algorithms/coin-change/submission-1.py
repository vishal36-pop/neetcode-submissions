class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        #basecase 
        for t in range(1,amount+1):
            dp[n][t] = 10000
        dp[n][0] = 0
        for i in range(n-1,-1,-1):
            for t in range(amount+1):
                if t >= coins[i]:
                    dp[i][t] = min(dp[i][t-coins[i]]+1 ,dp[i+1][t])
                else:
                    dp[i][t] = dp[i+1][t]

        return dp[0][amount] if dp[0][amount] != 10000 else -1