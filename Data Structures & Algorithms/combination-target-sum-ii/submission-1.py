class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        ans = []
        candidates.sort()
        l = len(candidates)
        def backtrack(i,prev,temp):
            if sum(temp) == target:
                ans.append(temp[:])
                return 
            if sum(temp) > target:
                return 
            for j in range(i,l):
                if j>i and  candidates[j]==candidates[j-1]:
                    continue
                if prev is None or candidates[j] >= prev :
                    temp.append(candidates[j])
                    backtrack(j+1,candidates[j],temp)
                    temp.pop()

        backtrack(0,None,temp)
        return ans

