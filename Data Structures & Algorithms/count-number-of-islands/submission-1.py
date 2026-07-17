class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #practice 

        #row,col
        row,col = len(grid),len(grid[0])
        #isvalid 
        def isvalid(r,c):
            return 0 <= r < row and 0 <= c < col
        #visited array 
        visited = [[False]*col for _ in range(row)]
        #dirs array for navigating
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r,c):
            #explore the neighbours and mark them visited
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if isvalid(nr,nc) and not visited[nr][nc] and grid[nr][nc] == '1':
                    visited[nr][nc] = True
                    dfs(nr,nc)
        #count the components
        count = 0
        for r in range(row):
            for c in range(col):
                if not visited[r][c] and grid[r][c] == '1':
                    visited[r][c] = True
                    dfs(r,c)
                    count+=1
        import numpy as np 
        print(np.array(visited))
        return count