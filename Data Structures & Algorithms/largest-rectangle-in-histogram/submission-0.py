class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        n = len(heights)

        for i in range(n):

            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()

                left = stack[-1] if stack else -1
                right = i

                width = right - left - 1
                ans = max(ans, heights[j] * width)

            stack.append(i)

        # Elements left in stack have no smaller element on the right
        while stack:
            j = stack.pop()

            left = stack[-1] if stack else -1
            right = n

            width = right - left - 1
            ans = max(ans, heights[j] * width)

        return ans