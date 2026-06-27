class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        count = list(count.items())
        return max(count ,key= lambda x : x[1])[0]