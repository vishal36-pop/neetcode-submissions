class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import deque
        import heapq

        freq = collections.Counter(s)
        heap = [(-f,ch) for ch,f in freq.items()]

        q = deque([])

        ans = ''

        t = 0
        while heap or q:
            while q and q[0][0] ==t:
                _,f,n = q.popleft()
                heapq.heappush(heap,(f,n))
            #if there are elements which can be choosen now 
            #if there are none return 
            #we cannot wait like the task scheduler 
            if heap :
                f,n = heapq.heappop(heap)
                ans+=n
                if f+1 <0:
                    q.append((t+2,f+1,n))
            else:
                return '' #not possible with the given condition
            t+=1
        return ans


