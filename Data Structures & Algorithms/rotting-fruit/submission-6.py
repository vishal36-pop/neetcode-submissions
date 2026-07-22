class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        import collections
        #this is a level order bfs
        row = len(grid)
        col = len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        sources = []
        #valid
        def valid(r,c):
            return 0<= r< row and 0<= c< col
        #count the no of fresh fruits
        fresh = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    sources.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        queue = collections.deque(sources)
        visited = [[False]*col for _ in range(row)]
        t = 0
        if fresh == 0:
            return 0
        fresh_left = fresh
        while queue:
            print(queue)
            n = len(queue)
            for _ in range(n):
                r,c = queue.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr,c+dc
                    if valid(nr,nc) and not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = 1
                        queue.append((nr,nc))
                        fresh_left -= 1
            t+=1
        return t-1 if fresh_left == 0 else -1
            

