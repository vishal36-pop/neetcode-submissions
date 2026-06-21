class MinStack:

    def __init__(self):
        self.stack = []
        self.mintill = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        currmin= val
        if not self.mintill:
            self.mintill.append(val)
        else:
            self.mintill.append(min(self.mintill[-1],val))
        print(self.mintill)
    def pop(self) -> None:
        self.mintill.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mintill[-1]
