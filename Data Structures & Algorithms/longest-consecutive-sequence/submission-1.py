class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        ans = -1
        for i in count:
            curr = 1
            j = i 
            while j+1 in count:
                curr+=1
                j+=1
            ans = max(ans,curr)
        return ans if ans >0 else 0
        