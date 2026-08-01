"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #the maximum no of intervals at conflict at time
        #so we want to sort the interval boundaries in two bucket start and end 
        #at the start of interval would would need a room 
        #if any interval ends at that time substart 1 from the active rooms
        #so we want active rooms at any point of time 
        #and get the max of that
        times = []
        for interval in intervals:
            times.append((interval.start,1)) # add one to active rooms
            times.append((interval.end,-1)) #remove one from the activerooms
        
        times.sort(key = lambda x: (x[0],x[1]))
        ans  =0 
        curr = 0
        for time in times:
            # simple strategy count the active rooms at this time 
            # first remove the room if meetind ends 
            # then only add if a meeting starts 
            curr+=time[1]
            ans = max(ans,curr)
        return ans