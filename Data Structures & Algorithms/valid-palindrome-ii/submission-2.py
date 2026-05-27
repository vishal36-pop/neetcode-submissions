class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        deleted = False
        def ispalindrome(s):
            l,r = 0,len(s)-1
            while l<=r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else :
                    return False
            return True
        while l<=r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else :
                break
        if l>r:
            return True
        s1 = s[:l]+s[l+1:]
        s2 = s[:r]+s[r+1:]
        return ispalindrome(s1) or ispalindrome(s2)
