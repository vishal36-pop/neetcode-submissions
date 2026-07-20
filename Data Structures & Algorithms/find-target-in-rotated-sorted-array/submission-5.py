class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #fidn the amount by which it is rotated
        l , r = 0 , len(nums)-1
        while l<r:
            mid = (l+r+1)//2
            if nums[0] < nums[mid]:
                l = mid
            else:
                r = mid-1
        #the l is the amount by which it is rotated
        print(l)

        if target < nums[0]:
            l,r = l+1 ,len(nums)-1
        else:
            l,r = 0,l
        print(l,r)
        while l <= r:
            mid = (l+r)//2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else :
                return mid
        return -1