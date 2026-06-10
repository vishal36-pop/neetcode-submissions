class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        path = []
        ans = []
        if digits == '':
            return []
        l = len(digits)
        def backtrack(i,path):
            #i represents which digit we are processing
            if i >= l:
                ans.append(''.join(path[:]))
                return
            for al in digitToChar[digits[i]]:
                path.append(al)
                backtrack(i+1,path)
                path.pop()
        backtrack(0,path)
        return ans
                