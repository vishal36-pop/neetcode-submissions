class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        target = len(word)
        temp = [] #backtrack variable
        dirs = [(0,-1),(-1,0),(0,1),(1,0)]
        row,col = len(board),len(board[0])
        visited = [[False]*col for _ in range(row)]
        def dfs(r,c,path:list):
            nw = ''.join(path)
            if nw == word :
                return True
            ans = False
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<row and 0<=nc<col and len(path)<len(word) :
                    #backtrack 
                    if visited[nr][nc] == True:
                        continue
                    path.append(board[nr][nc])
                    visited[nr][nc] = True
                    ans = dfs(nr,nc,path)
                    #path pop remove the element
                    path.pop()
                    visited[nr][nc] = False
                    if ans is True:
                        break
            return ans
        ans = False
        for r in range(row):
            for c in range(col):
                visited[r][c] = True
                ans = ans or dfs(r,c,[board[r][c]])
                visited[r][c] = False
                if ans :
                    break
            if ans:
                break
        return ans


            