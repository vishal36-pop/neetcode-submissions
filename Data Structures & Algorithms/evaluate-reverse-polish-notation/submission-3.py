class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop()+stack.pop())
            elif i == '-':
                stack.append(-(stack.pop()-stack.pop()))
            elif i == '*':
                stack.append(stack.pop()*stack.pop())
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                c = b/a
                if c < 0 :
                    stack.append(math.ceil(c))
                else :
                    stack.append(math.floor(c))
            else:
                stack.append(float(i))
            print(stack)
        return int(stack[-1])
            