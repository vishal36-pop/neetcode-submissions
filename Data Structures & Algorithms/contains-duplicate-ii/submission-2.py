class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = collections.defaultdict(int)
        i = 0 
        while i < len(nums):
            if nums[i] in hashmap and i - hashmap[nums[i]] <=k:
                return True
            else:
                hashmap[nums[i]] = i
            i+=1
            # print(hashmap)
        return False