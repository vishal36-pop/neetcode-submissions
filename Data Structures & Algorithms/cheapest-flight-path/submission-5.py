class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u,v,w in flights:
            adj[u].append((v,w))
        import heapq
        #we use the dist array to store the distances 
        #it has the shortest distance from source to it 
        # use an extra for no of edges between the nodes and source
        dist = [[float('inf')]*(k+2) for _ in range(n)] #airports are named from 0 to n-1
        dist[src][0] = 0 
        pq = [(0,src,0)]
        while pq:
            dist_u, u, noe= heapq.heappop(pq)
            if dist_u > dist[u][noe]:
                continue

            for v,w in adj[u]:
                if noe <= k and dist_u + w < dist[v][noe+1]:
                    dist[v][noe+1] = dist_u+w
                    heapq.heappush(pq,(dist[v][noe+1],v,noe+1))
                
        ans = min(dist[dst])
        return ans if ans < float('inf') else -1

