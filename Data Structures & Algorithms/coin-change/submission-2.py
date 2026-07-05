class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0 for _ in range(amount+1)]
        #basecase 
        for t in range(1,amount+1):
            dp[t] = 10000
        dp[0] = 0
        for i in range(n-1,-1,-1):
            for t in range(amount+1):
                if t >= coins[i]:
                    dp[t] = min(dp[t-coins[i]]+1 ,dp[t])
                else:
                    dp[t] = dp[t]

        return dp[amount] if dp[amount] != 10000 else -1