class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #initialize a table 
        dp = [[0]*n for _ in range(m)]
        #set the basecase to 0
        dp[m-1][n-1] = 1 # m-1,n-1 is reachable from itself in one way 
        #dp bottom up 
        max_size_pth = m-1+n-1
        for size in range(1,max_size_pth+1):
            for i in range(0,size+1):
            #calculate the dp table from smallest paths to longest paths
                x,y = m-1-i,n-1-(size-i)
                if x < 0 or y < 0 :
                    continue
                #only right
                if x == m-1 and y != n-1:
                    dp[x][y] = dp[x][y+1]
                #only left
                elif x != m-1 and y == n-1:
                    dp[x][y] = dp[x+1][y]
                else:
                    dp[x][y] = dp[x+1][y] + dp[x][y+1]
        print(dp)
        return dp[0][0]


        