class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        
        for s in strs:
            x = ''.join(sorted(s))
            hashmap[x].append(s)
        return list(hashmap.values())