class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        #form the adj and and indegree count
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1 
        
        #now the get the topological order 
        order = []
        #get the sources the indegree 0 nodes
        sources = []
        for i in range(numCourses):
            if indegree[i] == 0:
                sources.append(i)
        q = collections.deque(sources)
        while q :
            #pop the node in front of the queue which means this currently can be taken out 
            u = q.popleft()
            order.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return order if len(order) == numCourses else []