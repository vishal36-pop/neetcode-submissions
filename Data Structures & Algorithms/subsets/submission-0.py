class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        def backtrack(i,temp):
            if i>len(nums)-1:
                ans.append(temp[:])
                return 
            #add the nums[i] in the subsets
            temp.append(nums[i])
            backtrack(i+1,temp)
            #pop
            temp.pop()
            #explore the other choice which is no nums[i] in subsets
            backtrack(i+1,temp)
        backtrack(0,temp)
        return ans