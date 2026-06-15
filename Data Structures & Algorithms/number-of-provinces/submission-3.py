class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        size = [1 for i in range(len(isConnected))]
        l = len(isConnected)
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            ra = find(a)
            rb = find(b)
            
            sa = size[ra]
            sb = size[rb]
            if sa > sb:
                parent[rb] = ra
                size[ra]+=size[rb]
            else:
                parent[ra] = find(rb)
                size[rb]+=size[ra]
            return 
        for i in range(l):
            for j in range(l):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    union(i,j)

        #now we got the components its time to just group them 
        group = set()
        for i in range(l):
            r = find(i)
            group.add(r)
        return len(group)