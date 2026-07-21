class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        nums.sort()
        n = len(nums)
        #recursion
        def dfs(prev,temp,s):
            # print(temp,s)
            if s == target:
                ans.append(temp[:])
            if s > target:
                return
            for i in range(prev,n):
                temp.append(nums[i])
                s+=nums[i]
                #backtrack
                dfs(i,temp,s)
                #pop
                temp.pop()
                s-=nums[i]
        dfs(0,temp,0)
        return ans
