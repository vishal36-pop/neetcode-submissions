class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #use a stack
        stack = []
        print(int('-19'))
        print('-19'[1:].isdecimal())
        for op in operations:
            if op == '+':
                stack.append(stack[-1]+stack[-2])
            elif op == 'D':
                stack.append(stack[-1]*2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)   


