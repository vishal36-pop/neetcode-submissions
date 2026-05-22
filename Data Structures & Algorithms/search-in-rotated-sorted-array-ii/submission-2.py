class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 1,len(nums)
        #the searchspace is as above 
        while l < r :
            mid = (l+r)//2
            if nums[mid] <= nums[0] :
                r = mid 
            else :
                l = mid+1
        org_array = nums[l:]+nums[:l]
        l,r = 0,len(org_array)-1
        while l<=r :
            mid = (l+r)//2
            if target > org_array[mid] :
                l = mid+1
            elif target < org_array[mid]:
                r = mid-1
            else :
                return True 
        return False            

