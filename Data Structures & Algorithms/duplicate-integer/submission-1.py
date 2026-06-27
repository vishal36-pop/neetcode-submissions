class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for i in nums:
            if i not in visited:
                visited.add(i)
            else :
                return True 
        return False