class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #the greedy solution keep the jump which can reach the max dist 
        #keep the jump means keep the reach of the index that is max until curr including curr
        maxreach = 0
        l = len(nums)
        for i in range(len(nums)):
            if i > maxreach:
                #we can only take a decisoin at i if we can reach it 
                #we can not reach the i if it not in the max reach 
                #so stop there 
                return False
            if i+nums[i] > maxreach:
                maxreach = i+nums[i]
        if maxreach >= l-1:
            return True
        return False