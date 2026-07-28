class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        from functools import cache
        @cache
        def rec(i,curr_reach):
            if i > n-1:
                return 0
            if days[i] <=curr_reach:
                return rec(i+1,curr_reach)
            #one day pass
            one_day = costs[0] + rec(i+1,days[i])
            #seven day pass
            seven_day = costs[1] + rec(i+1,days[i]+6)
            #month 
            month = costs[2] + rec(i+1,days[i]+29)
            return min(one_day,seven_day,month)
        
        return rec(0,-1)