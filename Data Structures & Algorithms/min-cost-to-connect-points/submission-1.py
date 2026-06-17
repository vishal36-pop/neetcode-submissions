class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(u:list,v:list):
            return abs(u[0]-v[0])+abs(u[1]-v[1])
        #now we will do a prims algorithm which dont need a priority queue
        #if we maintain queue we will mantina a worst case vlogv
        #here E = o(v2) so dont maintain a priority queue we are better off iterating
        n = len(points)
        visited = [False for i in range(n)]
        dist = [float('inf') for i in range(n)]
        dist[0] = 0#first c = {0} we will grow this component
        #so when the n-1 edges are added to the c we will exit 
        ver = 0
        cost = 0
        nextnode = 0
        while ver<n:
            # add the nextnode to component c
            u = nextnode
            cost+=dist[u] #so dist[u] contains the least distance of u from component c 
            visited[nextnode] = True
            ver+=1
            nextnode = -1 #the nextnode which will be choosen from now
            #here we wiill search the next node to which there is a safe edge
            for i in range(n):
                #now we will see the next safe edge that can be added to the component c
                if visited[i]:
                    #already in the tree
                    continue
                #update the distance of this node the component 
                #dist[i] gives the dist from the component c before adding u 
                #so update if mh(u,i) < dist[i] then update else leave it currently its at min dist from the comp c
                dist[i] = min(dist[i],manhattan(points[u],points[i])) 
                if nextnode == -1 or dist[nextnode] > dist[i]:
                    nextnode = i
        return cost   
        
