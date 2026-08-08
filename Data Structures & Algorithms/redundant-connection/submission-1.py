class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        print(n)
        parent = [i for i in range(n+1)]
        size = [1 for i in range(n+1)]
        def find(x):
            if parent[x] == x:
                return x 
            parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            ra = find(a) # the element representing comp having a
            rb = find(b) # the element representing comp having b
            if ra == rb:
                # this means a and b are in same fucking component
                #so fucking return 
                return 
            if size[ra] > size[rb]:
                #add the rb component to ra
                #make the rb direct child of ra 
                parent[rb] = ra
                #increase the size of ra
                size[ra]+=size[rb]
            else :
                parent[ra] = rb
                size[rb]+=size[ra]
            return 
        #now iterate over the edges and merge the components together
        cycles = []
        for u,v in edges:
            rv = find(v)
            ru = find(u)
            if rv == ru:
                cycles.append([u,v])
            else:
                union(u,v)
        return cycles[-1]         