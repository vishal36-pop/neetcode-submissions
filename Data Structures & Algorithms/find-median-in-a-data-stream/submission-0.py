class MedianFinder:

    def __init__(self):
        self.nums = []
        self.l = 0

    def addNum(self, num: int) -> None:
        curr = self.l-1
        while curr >= 0 and self.nums[curr] > num :
            curr = curr-1
        # print(curr,self.nums)
        self.nums.insert(curr+1,num)
        # print(curr,self.nums)
        self.l += 1
    def findMedian(self) -> float:
        if self.l == 1:
            return self.nums[0]
        if self.l % 2:
            mid = self.l//2
            return self.nums[mid]
        else:
            # print(self.l,self.nums)
            mid = (self.l-1)//2
            return (self.nums[mid] + self.nums[mid+1])/2


