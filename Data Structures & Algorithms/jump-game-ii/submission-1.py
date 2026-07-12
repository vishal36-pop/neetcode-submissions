class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [l for _ in range(l)]
        #basecase is dp[l-1] = 0 > l-1 also 0
        dp[l-1] = 0 
        for i in range(l-2,-1,-1):
            ans = l
            for j in range(1,nums[i]+1):
                if i+j>l-1:
                    ans = min(ans,1+0)
                    continue
                ans = min(ans,1+dp[i+j])
            dp[i] = ans #if ans!= l else dp[i]
        return dp[0]
