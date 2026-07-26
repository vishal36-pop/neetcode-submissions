class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxheap = []
        minheap = []
        l = r = 0
        ans = 0
        def clear_heap(heap,l):
            while heap and heap[0][1] < l:
                heapq.heappop(heap)
        while r < len(nums):
            heapq.heappush(maxheap,(-nums[r],r))
            heapq.heappush(minheap,(nums[r],r))

            clear_heap(maxheap,l)
            clear_heap(minheap,l)
            
            while maxheap and minheap and abs(-maxheap[0][0] - minheap[0][0]) > limit:
                if minheap[0][1] < maxheap[0][1] :
                    l = minheap[0][1] +1 
                    heapq.heappop(minheap)
                else:
                    l = maxheap[0][1] + 1
                    heapq.heappop(maxheap)
                clear_heap(maxheap,l)
                clear_heap(minheap,l)
            ans = max(ans,r-l+1)
            r+=1
        return ans
                
