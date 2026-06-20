class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(1,0),(0,-1),(-1,0),(0,1)]
        temp = []
        row = len(board)
        col = len(board[0])
        visited = [[False]*col for _ in range(col)]
        def isvalid(r,c):
            return 0<=r<row and 0<=c<col
        def dfs(r,c,temp):
            if ''.join(temp) == word:
                return True
            check = False
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if isvalid(nr,nc) and visited[nr][nc] == False:
                    temp.append(board[nr][nc])
                    visited[nr][nc] = True
                    check = check or dfs(nr,nc,temp)
                    temp.pop()
                    visited[nr][nc] = False
            return check
        # visited[0][1]= True
        # print(dfs(0,1,['b']))
        ans = False
        for i in range(row):
            for j in range(col):
                print(i,j)
                visited[i][j] = True
                temp.append(board[i][j])
                ans = ans or dfs(i,j,temp)
                visited[i][j] = False
                temp.pop()
        return ans
