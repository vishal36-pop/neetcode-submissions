class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        for i in points:
            heap.append(i)
        return heapq.nsmallest(k,heap,lambda x: x[0]**2+x[1]**2)