class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [0]
        results = [0 for _ in range(n)]
        for i in range(1,n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                results[stack[-1]] = i-stack[-1]
                stack.pop()
            else:
                stack.append(i)
        return results