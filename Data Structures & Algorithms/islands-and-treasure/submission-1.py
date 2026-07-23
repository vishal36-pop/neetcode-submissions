class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        import collections
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        row = len(grid)
        col = len(grid[0])

        INF = 2147483647
        visited =  [[False]*col for _ in range(row)]

        def valid(r,c):
           return 0<=r<row and 0<=c < col

        sources = []
        #the land cell find the distance of the of each land cell to treasure chests
        #so each treasure is a source
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    sources.append((i,j))
                    visited[i][j] = True
        queue = collections.deque(sources)
        l = 0
        while queue :
            n = len(queue)
            for _ in range(n):
                r,c = queue.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr,c+dc
                    if valid(nr,nc) and not visited[nr][nc] and grid[nr][nc] == INF:
                        grid[nr][nc] = l+1
                        visited[nr][nc] = True
                        queue.append((nr,nc))
            l+=1



