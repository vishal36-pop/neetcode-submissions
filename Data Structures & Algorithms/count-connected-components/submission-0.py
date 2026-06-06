class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False for _ in range(n)]
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # we will do this question by dfs 
        def dfs(u):
            for v in adj[u]:
                if visited[v] == False:
                    visited[v] = True
                    dfs(v)
        count = 0
        for i in range(n):
            if visited[i] == False:
                count +=1
                visited[i] = True
                dfs(i)
        return count
            

