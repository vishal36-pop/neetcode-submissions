class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #edge cases 
        if nums == []:
            return 0
        if len(nums) == 1:
            return 0 if nums[0] >= target else 1
        #search the greatest element that is smaller than target 
        #search space is 0,len(nums)-1
        l,r = 0,len(nums)-1
        while l<r:
            mid = (l+r+1)//2
            if target > nums[mid]:
                l = mid 
            else:
                r = mid -1
        return l+1 if nums[l] < target else l