class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(weights,days,cap):
            curr = 0
            d = 1
            for i in weights:
                curr+=i
                if curr > cap:
                    curr = i 
                    d +=1
            return d <=days
        l,r = max(weights),sum(weights)
        while l<r :
            mid = (l+r)//2
            print(l,mid,r)
            if can_ship(weights,days,mid):
                r = mid 
            else :
                l = mid + 1
        return l

        