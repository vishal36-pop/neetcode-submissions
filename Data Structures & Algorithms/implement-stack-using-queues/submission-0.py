class MyStack:
    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()
    def push(self, x: int) -> None:
        self.q1.append(x)
    def pop(self) -> int:
        print(self.q1)
        while len(self.q1) > 1:
            a = self.q1.popleft()
            self.q2.append(a)
        ans = self.q1.popleft()
        self.q1 = self.q2
        self.q2 = collections.deque()
        return ans

    def top(self) -> int:
        while len(self.q1) > 1:
            a = self.q1.popleft()
            self.q2.append(a)
        ans = self.q1.popleft()
        self.q2.append(ans)
        self.q1 = self.q2
        self.q2 = collections.deque()
        return ans
    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()