class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i] 
        n = len(nums)
        dp = [1 for _ in range(len(nums))]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)