class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l <r:
            mid = (l+r+1)//2
            if nums[0] < nums[mid]:
                l = mid 
            else:
                r = mid-1
        #the l is last element in the original array sdo its the largest
        #and the next to it should be the smallest which is l+1 if l is len(nums)-1 then nums[0] is the smallest so 
        return nums[(l+1)%n]