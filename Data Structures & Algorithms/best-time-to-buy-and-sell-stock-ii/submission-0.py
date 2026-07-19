class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1]*2 for i in range(len(prices)+1)]
        l = len(prices)
        #basecase 
        dp[l][1] = 0
        dp[l][0] = 0
        for i in range(l-1,-1,-1):
            # #if i==0 only buy :
            # if i == 0:
            #     dp[i][0] = max(-prices[i]+dp[i+1][1],
            #                     dp[i+1][0])
            #     continue
            #sell
            dp[i][1] = max(prices[i]+dp[i+1][0],
                            dp[i+1][1]
                        )
            #buy 
            dp[i][0] = max(-prices[i]+dp[i+1][1],
                            dp[i+1][0])
        return dp[0][0]