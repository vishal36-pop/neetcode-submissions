class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp = []
        ans = []#array which contains the answers
        l = len(nums)
        def backtrack(prev,temp):
            if sum(temp) == target:
                ans.append(temp[:])
                return 
            if sum(temp) > target:
                return 
            #explore the choices and append
            for i in range(l):
                if prev is None or nums[i] >=prev :
                    temp.append(nums[i])
                    backtrack(temp = temp,prev= nums[i])
                    temp.pop()
        backtrack(temp= temp,prev = None)
        return ans