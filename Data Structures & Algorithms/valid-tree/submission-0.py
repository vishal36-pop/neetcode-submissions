class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        #start from 0 and do a bfs and check for an edge which creates a cycle 
        q = collections.deque()
        q.append(0)
        visited = [False]*(n)
        visited[0] = True
        parent = [-1 for _ in range(n)]
        #if there exist and edge between u which is being processed and v which is already visited 
        #so that edge creates a redundant edge which creates a cycle
        cycle = False
        while q :
            u = q.popleft()
            for  v in adj[u]:
                if visited[v] == False:
                    q.append(v)
                    parent[v] = u
                    visited[v] = True 
                elif visited[v] == True and parent[u] != v :
                    print(u,v)
                    cycle = True
                    break
            if cycle :
                break
        return not cycle if cycle else all(visited)

                    



        