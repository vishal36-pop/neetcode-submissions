class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #if we visit a node which is valid => not lies in the center then we will just change it to X if we encountered one 
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        row,col = len(board),len(board[0])
        sources = []

        for i in range(col):
            if board[0][i] == 'O':
                sources.append((0,i))
            if board[row-1][i] == 'O':
                sources.append((row-1,i))
        for i in range(1,row-1):
            if board[i][0] == 'O':
                sources.append((i,0))
            if board[i][col-1] == 'O':
                sources.append((i,col-1))
        #isvalid function
        def isvalid(r,c):
            return True if 0<=r<row and 0<=c<col else False
        #visited 
        visited = [[False]*(col) for _ in range(row)]
        #now do the dfs from all the sources on the boundaries to inside 
        def dfs(r,c):
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if isvalid(nr,nc) and board[nr][nc] == 'O' and not visited[nr][nc] :
                    visited[nr][nc] = True     
                    dfs(nr,nc)
        for r,c in sources:
            if not visited[r][c]:
                visited[r][c] = True
                dfs(r,c)
        for r in range(1,row-1):
            for c in range(1,col-1):
                if not visited[r][c]  :
                    board[r][c] = 'X'
        
                
            


                        

