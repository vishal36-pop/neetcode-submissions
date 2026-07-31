class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort()
        prevend = intervals[0][1]
        for i in intervals[1:]:
            if i[0] >= prevend:
                #no overlap
                prevend = i[1]
            else:
                prevend = min(i[1],prevend)
                ans+=1
        return ans

