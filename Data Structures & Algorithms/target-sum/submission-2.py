class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def rec(i,t):
            #rec(i) gives the no of ways to go to the target by using the i to len(nums)
            if i ==n and t == 0:
                return 1
            if i ==n and t != 0 :
                return 0
            #add to comb  
            a = rec(i+1,t-nums[i])
            #sub to comb
            b = rec(i+1,t+nums[i])
            
            return a+b
        return rec(0,target)