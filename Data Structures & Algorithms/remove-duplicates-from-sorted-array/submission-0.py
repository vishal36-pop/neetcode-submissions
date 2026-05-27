class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,0 
        n = len(nums)
        while r < len(nums):
            if r == len(nums)-1:
                while l<r:
                    nums[l] = None
                    l+=1
                r+=1
                continue
            if nums[r] == nums[r+1]:
                r+=1
                continue
            else :
                while l<r:
                    nums[l] = None
                    l+=1
                l+=1
                r+=1
        for i in nums[:]:
            if i is None:
                nums.remove(i)
        return len(nums)
