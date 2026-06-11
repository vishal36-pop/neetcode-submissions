class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #using the toposort we will now get all the ancestor in one fly
        #list of set which will store the prerequisites
        ances = [set() for _ in range(numCourses)]
        #adjacency and indegrees list 
        adj = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[u].append(v)
            indegrees[v]+=1
        #now get the sources the ndoes which have the indegrees as zero
        q = collections.deque()
        for i in range(numCourses):
            if indegrees[i] == 0 :
                q.append(i)
        #start the toposort
        while q:
            u = q.popleft()
            for v in adj[u]:
                # u is a prereq of the u 
                indegrees[v]-=1 #remove the constraint from the u 
                #add the u as prereq
                ances[v].add(u)
                ances[v].update(ances[u])#update the original set 
                if indegrees[v] == 0:
                    q.append(v)
        ans = []
        for u,v in queries:
            if u in ances[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans