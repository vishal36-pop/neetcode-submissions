class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        import heapq
        #using the greedy dijkstra approach the edges weights be grid[i][j] for any edge leaving the i,j
        #pq
        pq = [(0,0,0)]#w,i,j #priority is according to tentative shortest distance to source
        #dist array
        dist = [[float('inf')]*n for _ in range(m)]
        dist[0][0] = 0
        while pq:
            d,i,j = heapq.heappop(pq)
            if d > dist[i][j]:
                continue
            #now relax the neighbours of the i,j 
            #relax i+1,j
            if i  != m-1 and dist[i+1][j] >= grid[i][j] + d:
                dist[i+1][j] = grid[i][j]+d
                heapq.heappush(pq,(int(dist[i+1][j]),i+1,j))
            if j  != n-1 and dist[i][j+1] >= grid[i][j] + d:
                dist[i][j+1] = grid[i][j]+d
                heapq.heappush(pq,(int(dist[i][j+1]),i,j+1))
        return dist[m-1][n-1] + grid[m-1][n-1]