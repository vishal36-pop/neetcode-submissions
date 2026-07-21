class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = -1,len(matrix)-1
        while l<r:
            mid = (l+r+1)//2
            if target >=matrix[mid][0]:
                l = mid
            else:
                r = mid-1
        #search in the lth row 
        search_row = l
        print(l)
        l,r = 0,len(matrix[0])-1
        while l<=r:
            mid = (l+r)//2
            if target == matrix[search_row][mid]:
                return True
            elif target > matrix[search_row][mid]:
                l = mid + 1
            else :
                r = mid -1
        return False
