class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #counting Solution
        #the hashmap keys will be frequecy count of each character
        hashmap = collections.defaultdict(list)
        for s in strs:
            countmap = [0 for _ in range(26)]
            for ch in s:
                countmap[ord(ch)-ord('a')] +=1
            hashmap[tuple(countmap)].append(s)
        return list(hashmap.values())