class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        p = 0 
        ans = []
        while p <n-2:
            print(p)
            if p> 0 and nums[p-1] == nums[p]:
                p+=1
                continue
            q,r = p+1,n-1
            while q<r:
                s = nums[p]+nums[q]+nums[r]
                if s > 0 :
                    r-=1
                    continue
                if s < 0:
                    q+=1
                    continue
                else:
                    ans.append([nums[p],nums[q],nums[r]])
                    #now that the sum is 0 move either q to right or r to left 
                    q+=1
                    #now skip any duplicate
                    while q < n and nums[q] == nums[q-1]:
                        q+=1
            p+=1
        return ans

