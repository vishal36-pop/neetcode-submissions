class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,0 
        n = len(nums)
        ans = 0
        while r < len(nums):
            if r == len(nums)-1:
                while l<r:
                    nums[l] = None
                    l+=1
                    ans+=1
                r+=1
                continue
            if nums[r] == nums[r+1]:
                r+=1
                continue
            else :
                while l<r:
                    nums[l] = None
                    l+=1
                    ans+=1
                l+=1
                r+=1
        for i in range(ans):
            nums.remove(None)
        return len(nums)
