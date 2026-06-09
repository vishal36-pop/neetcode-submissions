class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r,l = 0,0
        ans = []
        path = []
        def backtrack(path):
            nonlocal r,l
            if len(path) == 2*n:
                ans.append(''.join(path))
                return 
            #our current state is path explore the options
            if r <n:
                path.append('(')
                r+=1
                #backtrack
                backtrack(path)
                path.pop()
                r-=1
            if r>l:
                path.append(')')
                l+=1
                backtrack(path)
                path.pop()
                l-=1
        backtrack(path)
        return ans

        