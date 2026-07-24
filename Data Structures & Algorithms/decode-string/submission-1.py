class Solution:
    def decodeString(self, s: str) -> str:

        n = len(s)
        i = 0
        stack = []
        while i < n :
            if s[i] == ']':
                j = i-1
                curr = ''
                while stack and  stack[-1] != '[' :
                    curr = stack.pop() + curr
                    print(curr)
                stack.pop()
                curr = curr*int(stack.pop())
                stack.append(curr)
            elif s[i].isnumeric():
                curr = ''
                while s[i].isnumeric():
                    curr+=s[i]
                    i+=1
                stack.append(curr)
                continue
            else:
                stack.append(s[i])
            i+=1
        return ''.join(stack)
                
