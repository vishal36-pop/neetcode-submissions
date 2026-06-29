from _heapq import heappop
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        from collections import deque
        
        q = sorted([(i,*j) for i,j in enumerate(tasks)],key = lambda x:x[1])
        minheap = []
        q = deque(q)
        time = 1
        ans = []
        while q or minheap :
            while q and q[0][1]  <= time:
                i,_,t = q.popleft()
                heapq.heappush(minheap,(t,i))
            if minheap:
                t,i = heapq.heappop(minheap)
                time+=t
                ans.append(i)
                continue
            time+=1
        return ans
            
            