class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        heapq.heapify(heap) #heapify is an inplace operation returns None
        origin = [0,0]
        def distance(x,y):
            return (x[0]-y[0])**2+(x[1]-y[1])**2
        for i in points:
            heapq.heappush(heap,(distance(i,origin),i))
        heapq.heapify(heap)
        ans = [i[1] for i in heapq.nsmallest(k,heap)]
        return ans
        

            
        