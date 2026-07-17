class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        currsum = 0
        ans = len(nums)+1
        while r < len(nums):
            currsum += nums[r]
            print(l,r)
            while currsum >= target:
                ans = min(ans,r-l+1)
                currsum -=nums[l]
                l+=1
            r+=1

        return ans if ans < len(nums)+1 else 0