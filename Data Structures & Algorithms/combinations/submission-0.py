class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = []
        ans = []
        #this is our current state 
        def backtrack(temp,prev = None):
            if len(temp) == k:
                ans.append(temp[:])
                return 
            #explore choices which can be explored from the current state:
            for num in range(1,n+1):
                #check if this num is a valid choice 
                #we dont want duplicate combinations so we only append this num if this is > prev 
                if prev is None or num > prev:
                    #append and recurse
                    temp.append(num)
                    backtrack(temp,prev = num)
                    #pop it 
                    temp.pop()
        backtrack(temp,prev = None)
        return ans 
                            

            