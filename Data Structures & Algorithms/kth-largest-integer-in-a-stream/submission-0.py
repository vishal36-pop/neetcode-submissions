class KthLargest:
    import heapq 
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        #keep only the top k largest elements in the heap
        while len(nums) > k:
            heapq.heappop(self.heap)
    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
