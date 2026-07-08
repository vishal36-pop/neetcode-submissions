class Solution:
    def reorganizeString(self, s: str) -> str:
        import heapq
        from collections import deque

        freq = collections.Counter(s).items()
        heap  =[(-i,j) for j,i in freq]
        heapq.heapify(heap)
        q = deque([])
        t = 0 
        #ans_str 
        ans = []
        while q or heap:
            # print('t:',t,'queue:',q,'heap:',heap,'ans:',ans)
            while q and q[0][0] <=t:
                _,f,n = q.popleft()
                heapq.heappush(heap,(f,n))
            if heap:
                #process
                f,n = heapq.heappop(heap)
                #queue it if f+1!= 0
                if f+1 !=0:
                    q.append((t+2,f+1,n))
                #add it to resulting string by rearraning
                ans.append(n)
            else:
                return ''
            t+=1
        return ''.join(ans)