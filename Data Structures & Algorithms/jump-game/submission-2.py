class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #use greedy 
        #using the hints provided
        n = len(nums)
        #initialize the reach array 
        goal = n-1
        for i in range(n-2,-1,-1):
            if i+nums[i]>=goal:
                goal = i
        if nums[0] >= goal:
            return True
        else:
            return False
    
            