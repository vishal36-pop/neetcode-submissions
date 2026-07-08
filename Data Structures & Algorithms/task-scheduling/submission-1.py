from _heapq import heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #so the hashmap consists of the tasks that are to be processed 
        #q consists of elements which are available at time t to above
        import heapq
        from collections import deque

        #the heap is max heap so - insert
        freq_count = collections.Counter(tasks).values()
        heap = [-i for i in freq_count]
        heapq.heapify(heap)
        q = deque([])
        t=0
        while q or heap:
            # print('t:',t,'queue:',q,'heap:',heap)
            while q and q[0][0] <=t :
                heapq.heappush(heap,q.popleft()[1])
            if heap:
                f = heapq.heappop(heap)
                if f+1 != 0:
                    q.append((t+n+1,f+1))
            t+=1
        return t