class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        def dfs(u,visited):
            count = 0
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    count = max(count,dfs(v,visited))
            return count+1
        h_arr = []
        for i in range(n):
            h_arr.append((i,dfs(i,set([i]))))
        h_arr.sort(key=lambda x:x[1])
        p = 1
        r = [h_arr[0][0]]
        print(h_arr)

        while p < n and h_arr[p][1]==h_arr[p-1][1]:
            r.append(h_arr[p][0])
            p+=1
        return r



            
                
        