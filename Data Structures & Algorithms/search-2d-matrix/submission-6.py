class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l,r=0,len(matrix[0])-1

        correct_row=0
        top,bottom = 0,len(matrix)-1
        while top<=bottom:
            mid = top+((bottom-top)//2)

            if matrix[mid][r]<target:
                top=mid+1
            elif matrix[mid][r]>target and matrix[mid][l]>target:
                bottom=mid-1
            else:
                correct_row=mid
                break
                
        while l<=r:
            mid = l+((r-l)//2)
            if matrix[correct_row][mid] == target:
                return True
            elif matrix[correct_row][mid] < target:
                l=mid+1
            else:
                r=mid-1
        return False

