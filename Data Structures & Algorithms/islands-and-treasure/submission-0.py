class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31-1
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        #visited array 
        visited = [[False]*len(grid[0])  for _ in  range(len(grid))]
        #multisources bfs problem sources are the treaures 
        sources = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    sources.append((r,c))
                    visited[r][c] = True
        q = collections.deque(sources)

        #d = [[float('inf')]*len(grid[0]) for _ in range(len(grid))]#distance array 
        #traverse 
        row = len(grid)
        col = len(grid[0])
        while q:
            r,c = q.popleft()

            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<row and 0<=nc<col and grid[nr][nc] != 0 and grid[nr][nc] != -1 :
                    if visited[nr][nc] == False :
                        q.append((nr,nc))
                        visited[nr][nc] = True
                    grid[nr][nc] = min(grid[nr][nc],grid[r][c]+1)

                    
                    
            

