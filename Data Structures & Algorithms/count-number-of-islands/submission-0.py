class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs_grid(source,visited):
            q = collections.deque([source])
            visited.add(source)
            while q:
                print(q)
                r,c = q.popleft()
                #explore the directions and add it to queue if its a land 
                for dr,dc in dirs:
                    nr,nc = r+dr,c+dc
                    print(nr,nc)
                    if (nr,nc) not in visited:
                        if 0<=nr<row and 0<=nc<col and grid[nr][nc] == "1":
                            visited.add((nr,nc))
                            q.append((nr,nc))
                            print(visited)

            return 
                     
        visited = set()
        row,col = len(grid),len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] =='1' and (r,c) not in visited:
                    bfs_grid((r,c),visited)
                    count+=1
        return count
                

