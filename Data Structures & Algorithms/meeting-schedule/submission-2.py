"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #if there is an overlap then true else false
        if len(intervals) == 0:
            return True
        intervals.sort(key = lambda x : x.start)
        # for interval in intervals:
        #     print(interval.start,interval.end)
        prevend = intervals[0].end
        for i in range(1,len(intervals)):
            if intervals[i].start >= prevend:
                prevend = intervals[i].end
                continue
            else:
                return False 
        return True 
