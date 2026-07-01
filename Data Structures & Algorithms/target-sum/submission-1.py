class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [[0]*(2*(sum(nums))+1) for _ in range(len(nums)+1)]
        n = len(nums)
        s = sum(nums)
        if target > s or target < -s:
            return 0
        #basecases 
        for t in range(2*s+1):
            if t == s:
                dp[n][t] = 1
            else:
                dp[n][t] = 0
        for i in range(n-1,-1,-1):
            for t in range(-s,s+1):
                if t+nums[i]+s <=2*s:
                    dp[i][t+s] = dp[i+1][t-nums[i]+s]+dp[i+1][t+nums[i]+s]
                else:
                    dp[i][t+s] = dp[i+1][t-nums[i]+s]
        return dp[0][target+s]