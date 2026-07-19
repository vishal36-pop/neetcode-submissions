class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = collections.Counter(t)
        l = r = 0
        ans = len(s)+1
        hashmap = collections.defaultdict(int)
        def helper(hashmap,tmap):
            for i in tmap:
                if hashmap[i] >= tmap[i]:
                    continue
                else :
                    return False
            return True
        curr = None
        while r < len(s):
            hashmap[s[r]] +=1
            while helper(hashmap,tmap) :
                if ans > r-l+1 :
                    ans = r-l+1
                    curr = (l,r)
                hashmap[s[l]] -= 1
                if hashmap[s[l]] == 0:
                    del hashmap[s[l]]
                l+=1
            r+=1
        if curr is None:
            return ''
        al,ar = curr
        return s[al:ar+1]
