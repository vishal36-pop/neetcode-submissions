class MedianFinder:
    import heapq
    def __init__(self):
        self.small,self.large = [],[]

    def addNum(self, num: int) -> None:
        #insert
        if self.large and num > self.large[0]:
            #the right side is the min heap
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-1*num)
        #balance
        #if left maxheap is greater by 1

        if len(self.small) > len(self.large)+1:
            val = heapq.heappop(self.small)
            #push to the min heap
            heapq.heappush(self.large,-1*val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            #push to the max heap
            heapq.heappush(self.small,-1*val)
        #at any point we can have max differnece of one size

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0

        
        