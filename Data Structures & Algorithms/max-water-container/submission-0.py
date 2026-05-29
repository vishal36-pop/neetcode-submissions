class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def volume(i,j):
            return min(heights[i],heights[j])*(j-i)
        i,j = 0,len(heights)-1
        ans = -1
        while i < j :
            ans = max(ans,volume(i,j))
            if heights[i]<heights[j]:
                i+=1
            else :
                j-=1
        return ans

            

