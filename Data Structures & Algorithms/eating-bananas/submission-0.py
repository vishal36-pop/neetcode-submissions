class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def caneat(k):
            ch = 0 
            for i in piles:
                ch+= math.ceil(i/k)
            return ch <=h 
        l,r = 1,max(piles)
        while l<r :
            mid = (l+r)//2
            if caneat(mid) :
                r = mid
            else:
                l = mid+1
        return l
