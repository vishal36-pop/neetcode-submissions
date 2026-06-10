class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       # we can finish only if there are no cycles that is a be prerequisite of b and b be of a at the same time 

        #adj
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[u].append(v)
        #visited 
        visited = [False for _ in range(numCourses)]
       #nodes visited in curr path 
        pathvis = [False for _ in range(numCourses)]
        def dfs(node):
            cycle = False
            for v in adj[node]:
                if visited[v] is False:
                    pathvis[v] = True
                    visited[v] = True
                    cycle = cycle or dfs(v)
                    pathvis[v] = False
                elif pathvis[v] == True:
                    #cycle is detected 
                    cycle = True
                    break
            return cycle
        ans = False
        for i in range(numCourses):
            if visited[i] == False:
                visited[i] = True
                pathvis[i] = True
                ans = ans or dfs(i)
                pathvis[i] = False
        return not ans
                

