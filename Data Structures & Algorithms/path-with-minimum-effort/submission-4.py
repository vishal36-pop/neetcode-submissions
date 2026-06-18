class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #relaxation step we want the path which has minimum effort from source to last so this is like min path weight 
        # if maxeffort = max(adjcent diff,maxeffort)
        #find shortest path from 0,0 to n-1,l-1
        maxeffort = [[1000000]*len(heights[0]) for i in range(len(heights))]
        maxeffort[0][0] = 0 
        row = len(heights)
        col = len(heights[0])
        import heapq
        def isvalid(r,c):
            return 0<=nr<row and 0<=nc<col
        pq = [(0,0,0)] #from 0 to 0 the min effor is 0
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        #use the dijkstra
        while pq :
            maxcurr,r,c = heapq.heappop(pq)
            if maxeffort[r][c] > maxcurr:
                continue
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if isvalid(nr,nc):
                   newmaxeffort = max(abs(heights[nr][nc] - heights[r][c]),maxeffort[r][c])
                   if newmaxeffort<maxeffort[nr][nc]:
                        maxeffort[nr][nc] = newmaxeffort
                        heapq.heappush(pq,(newmaxeffort,nr,nc))
        return maxeffort[row-1][col-1]