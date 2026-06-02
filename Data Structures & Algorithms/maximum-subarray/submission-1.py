class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_sum = nums[0]
        j = 0 
        while j < len(nums):
            curr= curr+nums[j]
            if curr >= 0 :
                max_sum = max(max_sum,curr)
                j+=1
                continue
            else:
                curr = nums[j]
                max_sum = max(max_sum,curr)
                j+=1
                #reset the curr
                curr = 0
        return max_sum


            

        