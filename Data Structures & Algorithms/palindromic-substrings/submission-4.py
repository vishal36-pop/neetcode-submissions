class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        #dp table
        dp = [[1 if (j-i == 1 and s[j]== s[i]) or j-i == 0 else 0 for j in range(len(s))] for i in range(len(s))]

        for j in range(n):
            for i in range(j,-1,-1):
                if j-i <=1:
                    count+=dp[i][j]
                    continue
                dp[i][j] = s[i]== s[j] and dp[i+1][j-1] 
                count+=dp[i][j]
        return count
