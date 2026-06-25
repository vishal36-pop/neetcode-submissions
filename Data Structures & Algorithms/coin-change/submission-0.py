class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [ 0 for _ in range(amount+1)]
        dp[0] = 0 
        for a in range(1,amount+1):
            ans = 100000000
            for d in coins:
                if a >=d:
                    ans = min(ans,dp[a-d])
            dp[a] = ans+1
        print(dp)
        return dp[amount] if dp[amount] < 100000000 else -1