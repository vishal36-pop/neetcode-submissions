class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        pvisited = [[False]*col for _ in range(row)]
        avisited = [[False]*col for _ in range(row)]
        psources = []
        asources = []
        for i in range(row):
            asources.append((i,col-1))
            psources.append((i,0))
        for i in range(col):
            asources.append((row-1,i))
            psources.append((0,i))
        
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(source,visited):
            #explore the neighbours
            r,c = source
            # print(source)
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<row and 0<=nc<col and visited[nr][nc] == False and heights[nr][nc] >= heights[r][c]:
                    # print(nr,nc)
                    visited[nr][nc] = True
                    dfs((nr,nc),visited)
        for i,j in psources:
            pvisited[i][j] = True
            dfs((i,j),pvisited)
        for i,j in asources:
            avisited[i][j] = True
            dfs((i,j),avisited)
        # import numpy as np
        # print(np.array(avisited),'\n',np.array(pvisited))
        ans= []
        for i in range(row):
            for j in range(col):
                if avisited[i][j] and pvisited[i][j]:
                    ans.append([i,j])
        return ans












