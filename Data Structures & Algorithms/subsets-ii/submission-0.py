class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ans = []
        path = []
        nums.sort()
        def backtrack(start,path):
            #basecase
            if len(path)<=l :
                ans.append(path[:])
            if start>=l:
                return
            #explore the choices from the current state
            for i in range(start,l):
                print(i)
                if i > start and nums[i] == nums[i-1]:
                    #skip the duplicate
                    continue
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,path)
        return ans

