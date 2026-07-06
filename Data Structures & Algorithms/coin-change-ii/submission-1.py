class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        #basecase
        dp[n][0] = 1
        #bottom up 
        for i in range(n-1,-1,-1):
            for t in range(amount+1):
                if t - coins[i] >=0 :
                    dp[i][t] = dp[i+1][t] + dp[i][t-coins[i]]
                else:
                    dp[i][t] = dp[i+1][t] 
        return dp[0][amount]