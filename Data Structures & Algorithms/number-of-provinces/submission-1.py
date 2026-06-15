class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: 
        l = len(isConnected)
        visited = [False for i in range(l)]

        def bfs(node):
            #we run bfs on i,j only if i,j was unvisited so we mark it visited and add it queue start bfs
            #for dfs its a little differnet mark it visited and then start the dfs
            q = collections.deque([node])

            visited[node] = True
            while q :
                u = q.popleft()
                for j in range(l):
                    if isConnected[u][j] ==1 and visited[j] == False:
                        visited[j] = True
                        q.append(j)
        count = 0
        for i in range(l):
            if visited[i] == False:
                count+=1
                bfs(i)
        return count


        