class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kandanes algorithm
        prev_max = nums[0]
        prev_min = nums[0]
        ans = prev_max
        for i in range(1,len(nums)):
            temp = prev_max*nums[i]
            prev_max = max(nums[i],prev_max*nums[i],prev_min*nums[i])
            prev_min = min(temp,nums[i],prev_min*nums[i])
            ans = max(prev_max,ans)
        return int(ans)