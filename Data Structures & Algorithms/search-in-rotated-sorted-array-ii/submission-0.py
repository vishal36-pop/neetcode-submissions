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
        ans = org_array.count(target)
        return bool(ans)
            

