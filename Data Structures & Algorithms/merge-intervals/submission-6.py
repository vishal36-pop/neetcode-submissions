class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr = intervals[0]
        def overlap(a,b):
            return a[1] >= b[0]
        ans = []

        for i in intervals[1:]:
            if overlap(curr,i):
                curr = [curr[0],max(curr[1],i[1])]
            else:
                ans.append(curr)
                curr = i
        ans.append(curr)
        return ans