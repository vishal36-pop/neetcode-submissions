class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n+2)]
        dp[n] = 0 
        dp[n+1] = 0
        for i in range(n-1,-1,-1):
            dp[i] = max(nums[i]+dp[i+2],dp[i+1])
        # print(dp)
        return dp[0]