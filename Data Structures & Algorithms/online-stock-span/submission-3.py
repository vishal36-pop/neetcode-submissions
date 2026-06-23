class StockSpanner:
    def __init__(self):
        self.prices = []
        self.stack = []
        self.size = 0
    def next(self, price: int) -> int:
        if not self.stack :
            self.stack.append(0)
            self.prices.append(price)
            self.size+=1
            return 1
        ans = 0
        # print(self.stack)
        # print(self.prices)
        # print(price)
        while self.stack and self.prices[self.stack[-1]]<=price:
            self.stack.pop()
        # print(self.stack)
        # print(self.size)
        if self.stack:
            ans = self.size-self.stack[-1]
        else :
            ans = self.size+1
        self.stack.append(self.size)
        self.prices.append(price)
        self.size+=1
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)