class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False]*(len(grid[0])) for _ in range(len(grid))]
        row = len(grid)
        col = len(grid[0])
        def valid(r,c):
            return 0 <= r < row and 0 <= c< col and grid[r][c] == 1
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r,c) :
            print(r,c)
            count =1 
            for dr,dc in dirs :
                nr,nc = r+dr,c+dc 
                if valid(nr,nc) and visited[nr][nc] == False :
                    visited[nr][nc] = True
                    count += dfs(nr,nc)
            return count
        count = 0 
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    visited[r][c] = True
                    count = max(count,dfs(r,c))
        return count


            