class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        import heapq
        for i in nums:
            if len(heap) < k:
                heapq.heappush(heap,i)
            else:
                a = heap[0]
                if a < i:
                    heapq.heappop(heap)
                    heapq.heappush(heap,i)
        return heap[0]


    
