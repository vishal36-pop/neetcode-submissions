class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq 
        minheap = []
        size = 0 
        hashmap = collections.Counter(nums)
        for i in hashmap:
            if size < k:
                heapq.heappush(minheap,(hashmap[i],i))
                size+=1
            else :
                freq,_ = minheap[0]
                if freq < hashmap[i]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap,(hashmap[i],i))
        return [x[1] for x in minheap]