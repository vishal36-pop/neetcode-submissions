class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        hashmap = defaultdict(list)
        for ndx,num in enumerate(nums):
            hashmap[num].append(ndx)
        for num in nums:
            if target-num not in hashmap:
                continue
            if target-num == num:
                if len(hashmap[num])>1:
                    return hashmap[num]
            else:
                return [hashmap[num][0],hashmap[target-num][0]]   
                    


        

        
        