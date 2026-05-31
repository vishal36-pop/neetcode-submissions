class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 :
            return 0
        l,r = 1,x #the search space and we may have the solution or nearest solution
        #largeest interger who is square is <= x 
        ans = -1
        while l<=r :
            mid = (l+r)//2
            if mid*mid <= x:
                ans = mid
                l= mid+1
            else:
                r = mid-1
        return ans

        