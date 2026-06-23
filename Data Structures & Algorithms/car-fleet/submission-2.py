class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pands = [(i,j) for i,j in zip(position,speed)]
        pands.sort(key=lambda x:x[0])
        stack = []
        for i,j in pands:
            if not stack:
                stack.append((i,j))
                continue
            while stack and stack[-1][1] > j and (i-stack[-1][0])/(stack[-1][1]-j) <= (target-i)/j:
                stack.pop()
            else:
                stack.append((i,j))
        return len(stack)