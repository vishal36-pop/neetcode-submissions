class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap= collections.defaultdict(int)
        l,r = 0,len(s1)-1
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            hashmap[s2[i]] +=1
        per = collections.Counter(s1)
        while r < len(s2):
            if per == hashmap:
                return True
            hashmap[s2[l]]-=1
            if hashmap[s2[l]] == 0:
                del hashmap[s2[l]]
            l+=1
            r+=1
            if r < len(s2):
                hashmap[s2[r]]+=1
        return False