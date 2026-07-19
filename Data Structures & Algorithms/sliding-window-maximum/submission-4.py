class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_ndx = 0
        l,r = 0,k-1
        heap = []
        import heapq
        ans = []
        for i in range(k):
            heapq.heappush(heap,(-1*nums[i],i))
        ans.append(-1*heap[0][0])
        # print(heap)
        count = 1
        while r+1< len(nums):
            l+=1
            while heap and heap[0][1] < l :
                heapq.heappop(heap)
            heapq.heappush(heap,(-1*nums[r+1],r+1))
            ans.append(-1*heap[0][0])
            r+=1
            # print(heap)
        return ans
