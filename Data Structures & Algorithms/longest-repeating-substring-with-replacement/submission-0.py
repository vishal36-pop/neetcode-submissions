class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        hashmap = collections.defaultdict(int)
        maxfreq = 1
        ans = 0
        while r < len(s):
            hashmap[s[r]] += 1
            maxfreq = max(maxfreq,hashmap[s[r]])
            while r-l+1 - maxfreq > k:
                # means the the number of replace chars are > k so reduce the window until
                hashmap[s[l]]-=1
                maxfreq = max(maxfreq,hashmap[s[l]])
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans


