class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False for _ in range(len(nums))]
        size = len(nums)
        path = []
        ans = []
        def backtrack(path):
            if len(path) == size:
                ans.append(path[:])
                return 
            for i in range(size):
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i] = True
                backtrack(path)
                path.pop()
                visited[i] = False
        backtrack(path)
        return ans
                
