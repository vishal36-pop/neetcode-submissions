class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if matrix[0][0]> target:
            return False
        if matrix[m-1][n-1] < target :
            return False
        
        #find the row the element belongs to
        #so find the largest element less than or equal to the target along the axis = 0 along col 1 to find the row

        #binary search terminates when the search space is empty i.e (l>r)
        l,r = 0,m-1
        while l<= r:
            mid = (l+r)//2
            if target > matrix[mid][0]:
                l = mid+1
            elif target < matrix[mid][0]:
                r = mid-1
            else:
                break
        row_no = (l+r)//2
        #now find the col in row using binary search
        l,r = 0,n-1
        while l<=r:
            mid = (l+r)//2
            if target > matrix[row_no][mid]:
                l = mid+1
            elif target < matrix[row_no][mid]:
                r = mid-1
            else:
                return True
        return False


        