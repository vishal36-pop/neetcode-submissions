class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        #dp 
        dp = [0 for _ in range(target+1)]
        #base case = 0 one combination
        dp[0] = 1
        for i in range(target+1):
            for num in nums:
                if i - num >=0:
                    dp[i] += dp[i-num]
        print(dp)
        return dp[target]