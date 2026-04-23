class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[n-1] = True
        for i in range(n-2,-1,-1):
            if nums[i] == 0 :
                dp[i] = True
            dp[i] = False
            for j in range(1,nums[i]+1):
                dp[i] = dp[i] or dp[i+j]
        return dp[0]
        