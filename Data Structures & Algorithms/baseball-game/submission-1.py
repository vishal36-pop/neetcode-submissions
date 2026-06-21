class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #use a stack
        stack = []
        print(int('-19'))
        print('-19'[1:].isdecimal())
        for op in operations:
            print(stack)
            print(op)
            
            if op.startswith('-') and op[1:].isnumeric():
                stack.append(int(op))
            if op.isnumeric():
                stack.append(int(op))
            if op == '+':
                stack.append(stack[-1]+stack[-2])
            if op == 'D':
                stack.append(stack[-1]*2)
            if op == 'C':
                stack.pop()
        return sum(stack)   


