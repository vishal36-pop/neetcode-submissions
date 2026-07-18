class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        ans = 0
        for i in range(len(prices)):
            minbuy = min(minbuy,prices[i])
            ans = max(ans,prices[i] - minbuy)
        return ans