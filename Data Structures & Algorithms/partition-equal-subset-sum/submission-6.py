class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2:
            return False
        #the recursion is 
        #rec(i,t) = rec(i+1,t) or rec(i+1,t-nums[i]) # take it or leave it or recursion
        n = len(nums)
        target = sum(nums)//2
        print(target)
        dp = [[False]*(target+1) for _ in range(n+1)]
        for t in range(1,target+1):
            dp[n][t] = False
        dp[n][0] = True
        #base case i = n and target = 0 True
        for i in range(n-1,-1,-1):
            for t in range(target+1):
                dp[i][t] = dp[i+1][t] or dp[i+1][t-nums[i]]
        return dp[0][target]
