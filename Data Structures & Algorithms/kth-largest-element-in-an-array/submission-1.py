class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        minheap = []
        no = 0
        for num in nums:
            if no < k:
                heapq.heappush(minheap,num)
                no+=1
                continue
            elif minheap[0] < num:
                heapq.heappop(minheap)
                heapq.heappush(minheap,num)
        return minheap[0]