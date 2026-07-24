class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1+n2 != len(s3):
            return False
        #we want dp[i][j] is the s1[i:] s2[j:]
        #if at the end both the strings are completely exhausted then true
        dp = [[False]*(n2+1) for _ in range(n1+1)]
        dp[n1][n2] = True

        for j in range(n2,-1,-1):
            for i in range(n1,-1,-1):
                if i < n1 and s3[i+j] == s1[i]:
                    dp[i][j] = dp[i][j] or dp[i+1][j]
                if j < n2 and s3[i+j] == s2[j]:
                    dp[i][j] = dp[i][j] or dp[i][j+1]
        return dp[0][0]