class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = r = 0
        ans = 0
        while r < len(s):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(s[r])
            ans = max(ans,r-l+1)
            r+=1
        return ans
