class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        sources = []
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    sources.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1
        #if the fresh fruits are zero 
        if not fresh :
            return 0
        row = len(grid)
        col = len(grid[0])
        q = collections.deque(sources)
        dirs = [(1,0),(0,1),(0,-1),(-1,0)]
        #level bfs with multisources in grid
        visited = set()
        for s in sources :
            visited.add(s)
        time = 0 # each level the time increases by 1
        while q :
            l = len(q)
            for _ in range(l):
                r,c = q.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1:
                        if (nr,nc) not in visited:
                            fresh-=1
                            visited.add((nr,nc))
                            q.append((nr,nc))
            time+=1
        return (-1 if fresh else time-1)



                
