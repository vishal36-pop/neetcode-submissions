class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def isiso(s,t):
            hashmap = {}
            for c,d in zip(s,t):
                if c in hashmap and hashmap[c] != d:
                    return False
                hashmap[c] = d
            return  True
        return isiso(s,t) and isiso(t,s)