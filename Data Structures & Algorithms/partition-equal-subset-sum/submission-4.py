class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot_sum = sum(nums)
        if tot_sum % 2 !=0 :
            return False
        target = tot_sum//2
        n = len(nums)
        dp = [[0]*(target+1) for _ in range(n+1)]
        #fill this dp in bottom up
        for i in range(n+1):
            dp[i][target] = 1
        for i in range(n-1,-1,-1):
            for t in range(target+1):
                temp = t + nums[i]
                if temp > target :
                    dp[i][t] = dp[i+1][t]
                else:
                    dp[i][t] = dp[i+1][t] or dp[i+1][temp]
        from numpy import array
        print(array(dp))
        return bool(dp[0][0])