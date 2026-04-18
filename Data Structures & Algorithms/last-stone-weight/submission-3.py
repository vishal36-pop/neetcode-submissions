class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones.sort()
        while len(stones) > 1:
            w1 = stones[-1]
            w2= stones[-2]
            stones[-2] = abs(w1-w2)
            stones.pop()
            stones.sort()
        return stones[0]
