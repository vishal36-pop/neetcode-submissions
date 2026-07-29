class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[1])
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            temp = intervals[i]
            while ans and temp[0] <= ans[-1][1]:
                temp = [min(ans[-1][0],temp[0]),temp[1]]
                ans.pop()
            else:
                ans.append(temp)

        return ans
