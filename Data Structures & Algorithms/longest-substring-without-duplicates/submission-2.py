class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l,r = 0,0
        #let the hashmap store the lastoccurence of the char
        hashmap = collections.defaultdict()
        while r < len(s):
            #reduce the window to l+1 where l is the last occurenec eof the r 
            #and we will only check in curr window l,r 
            if s[r] in hashmap:
                if hashmap[s[r]] >= l :
                    l = hashmap[s[r]]+1
            hashmap[s[r]] = r 
            ans = max(ans,r-l+1)
            r+=1    
        return ans