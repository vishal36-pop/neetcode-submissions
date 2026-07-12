class Solution:
    def jump(self, nums: List[int]) -> int:
        #greedy Solution
        l,r = 0,0
        count = 0
        while r < len(nums)-1:
            max_reach = 0
            for i in range(l,r+1):
                max_reach = max(max_reach,i+nums[i])
            l = r+1
            r = max_reach
            count+=1
        return count