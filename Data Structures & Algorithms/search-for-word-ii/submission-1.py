class Solution:

    def check(self,board, position, word) -> bool:
        visited = set()
        row = position[0]
        col=position[1]
        for i,c in enumerate(word):
            if i==0:
                visited.add(position)
                continue
            if (row-1 >=0 and board[row-1][col] == c and (row-1,col) not in visited):
                visited.add((row-1,col))
                row=row-1
                continue
            elif (row+1<=len(board)-1 and board[row+1][col]==c and (row+1,col) not in visited):
                visited.add((row+1,col))
                row=row+1
                continue
            elif (col-1>= 0 and board[row][col-1]==c and (row,col-1) not in visited):
                visited.add((row,col-1))
                col=col-1
                continue
            elif (col+1 <= len(board[0])-1 and board[row][col+1]==c and (row,col+1) not in visited):
                visited.add((row,col+1))
                col=col+1
                continue
            else:
                return False
        return True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        for word in words:
            visited = {}

            for row_index, row in enumerate(board):
                for col_index, letter in enumerate(row):
                    if letter == word[0]:
                        found = self.check(board, (row_index,col_index),word)
                        if found:
                            res.add(word)
        
        return list(res)