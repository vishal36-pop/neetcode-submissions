class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        maxheap = []
        i = 0
        ans = []
        while i < len(nums):
            # print(maxheap)
            if i < k-1:
                heapq.heappush(maxheap,(-nums[i],i))
                i+=1
                continue
            while maxheap and maxheap[0][-1] < i-k+1:
                heapq.heappop(maxheap)
            heapq.heappush(maxheap,(-nums[i],i))
            ans.append(-maxheap[0][0])
            i+=1
        return ans
