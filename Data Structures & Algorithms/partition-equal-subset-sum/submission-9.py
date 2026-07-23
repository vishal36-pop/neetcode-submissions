class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        n = len(nums)
        if S % 2:
            return False
        target = S//2
        dp = [[False]*(target+1) for _ in range(n+1)]
        #basecase
        dp[n][0] = True
        
        for i in range(n-1,-1,-1):
            for t in range(0,target+1):
                if t - nums[i] >=0 :
                    dp[i][t] = dp[i+1][t-nums[i]] or dp[i][t]
                dp[i][t] = dp[i][t] or dp[i+1][t]

        import numpy 
        print(numpy.array(dp))
        return dp[0][target]