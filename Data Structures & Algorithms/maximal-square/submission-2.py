class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dirs = [ 
            (1,0,1,0),
            (1,0,0,-1),
            (0,-1,1,0),
            (0,-1,0,-1)
        ]
        from functools import cache
        @cache
        def rec(lx,rx,ly,ry):
            if lx == rx and ly == ry and matrix[lx][ly] == '1' :
                return 1,True
            elif lx == rx and ly == ry and matrix[lx][ly] == '0':
                return 0,False
            ans = 0
            f = True
            for dlx,drx,dly,dry in dirs:
                nlx,nrx,nly,nry = lx+dlx,rx+drx,ly+dly,ry+ dry
                x,flag = rec(nlx,nrx,nly,nry)
                f = f and flag
                ans = max(ans,x)
            return ((rx-lx+1)*(ry-ly+1),f) if f else (ans,f)

        m = len(matrix)
        n = len(matrix[0])
        if m > n :
            l,r = 0,n-1
            ans = 0
            while r<m:
                curr,flag = rec(l,r,0,n-1)
                ans = max(ans,curr)
                l+=1
                r+=1
            return ans
        else:
            l,r = 0,m-1
            ans = 0
            while r<n:
                curr,flag = rec(0,m-1,l,r)
                ans = max(ans,curr)
                l+=1
                r+=1
            return ans

            
