class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0]*len(s) for _ in range(len(s))]
        max_len = -1
        max_str = ''
        for j in range(len(s)):
            for i in range(j+1):
                if i==j:
                    dp[i][j] = 1
                elif j-i==1:
                    if s[i]==s[j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 0
                if dp[i][j]:
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        max_str = s[i:j+1]
        return max_str



        