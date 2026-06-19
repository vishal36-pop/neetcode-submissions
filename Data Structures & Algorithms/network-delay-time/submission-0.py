class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        adj = [[] for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        #dist
        dist = [1000001 for _ in range(n+1)]
        dist[0] = -1
        dist[k] = 0 
        #start node is k 
        pq = [(0,k)] #initially the closest node to source is source itself
        while pq:
            w,u = heapq.heappop(pq)
            #the heapq contain the node u many times since it might have been relaxed from multiple nodes
            #we always pop the min one so we can always ignore u whenever encounter it again use a visited set 
            # or dist[u] < w : continue since u is already at at shortest distance possible
            if dist[u] < w:
                continue
            for v,w in adj[u]:
                #relax its neighbours
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq,(dist[v],v))
        ans = max(dist)
        return ans if ans<1000001 else -1