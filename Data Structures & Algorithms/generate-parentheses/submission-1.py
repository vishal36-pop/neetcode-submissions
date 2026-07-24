class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        ans = []

        def backtrack(l,r):
            if l+r == 2*n:
                ans.append(''.join(temp))
                return 
            if l < n:
                temp.append('(')
                l+=1
                backtrack(l,r)
                temp.pop()
                l-=1
            if r<l:
                temp.append(')')
                r+=1 
                backtrack(l,r)
                temp.pop()
                r-=1
        backtrack(0,0)
        return ans