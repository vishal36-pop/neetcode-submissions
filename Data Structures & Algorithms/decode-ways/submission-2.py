class Solution:
    def numDecodings(self, s: str) -> int:
        #dp table 
        dp = [0]*(len(s)+1)
        valid_strs = [f'{i}' for i in range(1,27)]
        dp[-1] =1 
        #basecases
        if s[-1] in valid_strs:
            dp[-2] = 1
        else:
            dp[-2] = 0 
        for j in range(len(s)-2,-1,-1):
            v_j = s[j] in valid_strs
            v_j1 = s[j:j+2] in valid_strs 
            if v_j and v_j1:
                dp[j] = dp[j+1]+dp[j+2]
            elif v_j and not v_j1:
                dp[j] = dp[j+1]
            elif not v_j and v_j1:
                dp[j] = 0
            else:
                dp[j] = 0
        print(dp)
        return dp[0]