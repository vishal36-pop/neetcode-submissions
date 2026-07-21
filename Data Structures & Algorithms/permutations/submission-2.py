class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        visited = set()
        #all possible permutations
        n = len(nums)
        def dfs(l):
            if l == n:
                ans.append(temp[:])
            #backtracking
            for i in nums:
                if i in visited:
                    continue
                #backtrack
                visited.add(i)
                temp.append(i)
                dfs(l+1)
                #pop
                visited.remove(i)
                temp.pop()
        dfs(0)
        return ans
