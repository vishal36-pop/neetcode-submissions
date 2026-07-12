class Solution:
    def jump(self, nums: List[int]) -> int:
        #optimized dp Solution
        l = len(nums)
        dp = [l for _ in range(l)]
        #l-1 case
        dp[l-1] = 0 #becuase we are already at l-1
        #aim is to reach by taking min steps from i to l-1
        #at i we can go to i+nums[i]th index at max
        for i in range(l-2,-1,-1):
            for j in range(1,nums[i]+1):
                if i+j>=l-1:
                    dp[i] = 1  #one step to reach >= l-1 index so thats it 
                    break
                dp[i] = min(dp[i],1+dp[i+j])
        return dp[0]