class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_rows = len(matrix)
        top = 0
        bot = len_rows-1
        while top<=bot:
            row = top + ((bot-top)//2)
            if target>matrix[row][-1]:
                top = row+1
            elif target<matrix[row][0]:
                bot = row-1
            else:
                break
        if not (top<=bot):
            return False
        
        row = (top+bot)//2

        l,r = 0, len(matrix[row])-1
            
        while l<=r:
            m = l + ((r-l)//2)
            if target > matrix[row][m]:
                l+=1
            elif target < matrix[row][m]:
                r-=1
            else:
                return True
        return False
                
