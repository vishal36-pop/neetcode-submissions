class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for i in nums:
            if i in visited:
                return i
            else :
                visited.add(i)
                