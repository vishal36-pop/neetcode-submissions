import heapq
from collections import deque
        
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        q = sorted([(i,*j) for i,j in enumerate(tasks)],key = lambda x:x[1])
        minheap = []
        q = deque(q)
        time = q[0][1] #start time is the first  #the start time of the first task
        ans = []
        while q or minheap :
            while q and q[0][1] <= time:
                i,_,p = q.popleft()
                heapq.heappush(minheap,(p,i)) 
            if minheap:
                p,i = heapq.heappop(minheap)
                ans.append(i)
                time +=p
            else:
                time = q[0][1]
        return ans
            
            