class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        p = 0
        n = len(nums)
        ans = []
        while p < n-2:
            if p > 0 and nums[p] == nums[p-1]:
                p+=1
                continue
            q,r = p+1,n-1
            while q < r :
                s = nums[p]+nums[q]+nums[r]
                if s > 0 :
                    r-=1
                elif s < 0:
                    q +=1
                else :
                    ans.append([nums[p],nums[q],nums[r]])
                    #skip duplicates of q,r
                    r-=1
                    while nums[r] == nums[r+1] and r>0:
                        r-=1
                    
            p+=1
        return ans
        



