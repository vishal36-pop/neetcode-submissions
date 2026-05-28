class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        #pointer a
        a = 0
        n = len(nums)
        ans = []
        while a < n-3:
            if  a > 0 and nums[a] == nums[a-1] : 
                a+=1
                continue
            b = a+1 #pointer b
            while b < n-2 :
                if  b>a+1 and nums[b] == nums[b-1] : 
                    b+=1
                    continue
                c,d = b+1,n-1
                while c<d:
                    s = nums[a]+nums[b]+nums[c]+nums[d]
                    if s > target :
                        d-=1
                    elif s < target :
                        c +=1
                    else :
                        ans.append([nums[a],nums[b],nums[c],nums[d]])
                        c+=1
                        while c<n and c > 0 and nums[c] == nums[c-1]:
                            c+=1
                b+=1
            a+=1
        return ans 

