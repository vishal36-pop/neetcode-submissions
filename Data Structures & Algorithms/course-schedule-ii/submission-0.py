class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #do a topo sort with kahns 
        topo = []
        #adjacency List
        adj = [[] for _ in range(numCourses)]
        #indegrees
        indegrees = [0 for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
            indegrees[u]+=1
        #queue
        sources = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                sources.append(i) 
        q = collections.deque(sources)
        while q:
            u = q.popleft()
            topo.append(u)
            for v in adj[u]:
                indegrees[v]-=1
                if indegrees[v] == 0:
                    q.append(v)
        if len(topo) == numCourses :
            #this means we have ALL THE nodes in topo so valid topo no cycles
            return topo
        else:
            return []