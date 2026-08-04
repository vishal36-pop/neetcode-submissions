class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0 for _ in range(n)]
        def add(stack,i):
            while stack and heights[i] > heights[stack[-1]]:
                ans[stack[-1]] +=1
                stack.pop()
            else:
                if stack :
                    ans[stack[-1]]+=1
                stack.append(i)
        stack = []
        for i in range(n):
            add(stack,i)
        return ans
                