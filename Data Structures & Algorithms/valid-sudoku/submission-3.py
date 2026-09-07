class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # set per row
        # set per colummn
        # set per square
        # (0,0) (0,1) (0,2) (1,0)... (2,2)
        unique_rows = [set() for _ in range(9)]
        unique_columns = [set() for _ in range(9)]
        unique_squares = dict() # key: tuple ; value: set

        for i, row in enumerate(board):
            for j,col in enumerate(row):
                val = board[i][j]
                if val == ".":
                    continue
                else:
                    val = int(val)
                if val in unique_rows[i]:
                    return False
                unique_rows[i].add(val)
                if val in unique_columns[j]:
                    return False
                unique_columns[j].add(val)
                t = (i//3,j//3)
                if t in unique_squares:
                    if val in unique_squares[t]:
                        return False
                    unique_squares[t].add(val)
                else:
                    unique_squares[t] = set()
                    unique_squares[t].add(val)

        return True
