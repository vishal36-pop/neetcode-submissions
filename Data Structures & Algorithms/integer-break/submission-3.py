class Solution:
    def integerBreak(self, n: int) -> int:
        from functools import cache
        @cache
        def rec(i):
            #base
            if i == 1:
                return 1
            res = -1
            for j in range(1,i+1):
                res = max(rec(i-j)*j,(i-j)*j,res)
            return res
        return rec(n)