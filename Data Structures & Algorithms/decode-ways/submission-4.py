class Solution:
    def numDecodings(self, s: str) -> int:
        valid_strs = set([str(i) for i in range(1,27)])
        n = len(s)
        if n ==1 :
            return 1 if s in valid_strs else 0
        if n==2 :
            a = s[n-2] in valid_strs and s[n-1] in valid_strs
            b = s in valid_strs
            return 2 if a and b else 1 if a or b else 0
        dp = [0 for _ in range(n)]
        dp[n-1] = 1 if s[n-1] in valid_strs else 0
        a = s[n-2] in valid_strs and s[n-1] in valid_strs
        b = s[n-2:] in valid_strs

        dp[n-2] = 2 if a and b  else 1 if a or b else 0

        for i in range(n-3,-1,-1):
            a = s[i] in valid_strs
            b = s[i:i+2] in valid_strs
            #if s[i] is valid and s[i:i+2] is valid
            if a and b:
                dp[i] = dp[i+1] + dp[i+2]
            if a and not b:
                dp[i] = dp[i+1]
            if not a :
                dp[i] = 0
        return dp[0]