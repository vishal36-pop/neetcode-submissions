class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 1,len(nums)
        while l<r :
            mid = (l+r+1)//2
            if nums[0] > nums[mid-1] :
                r = mid-1
            else:
                l = mid
        return nums[0] if l == len(nums)  else nums[l]



        