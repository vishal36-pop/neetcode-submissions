class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        row = len(grid)
        col = len(grid[0])

        def isvalid(r,c):
            return 0<=nr<row and 0<=nc<col
        
        dist = [[1000000]*len(grid) for _ in range(len(grid[0]))]

        pq = [(0,0,0)]
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        dist[0][0] = grid[0][0]

        while pq:
            w,r,c = heapq.heappop(pq)
            print(w,r,c)
            if w > dist[r][c]:
                continue

            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if isvalid(nr,nc):
                    #relaxation
                    max_elev = max(dist[r][c],grid[nr][nc]) #max elev of s---->u->v is this 
                    if dist[nr][nc] > max_elev:
                        dist[nr][nc] = max_elev
                        heapq.heappush(pq,(max_elev,nr,nc))
        return dist[row-1][col-1]

