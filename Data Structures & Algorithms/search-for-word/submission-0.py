class TrieNode:
    def __init__(self):
        self.pointers = {}
        self.isWord = False

    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.pointers:
                curr.pointers[c] = TrieNode()
            curr = curr.pointers[c]
        curr.isWord=True


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        root = TrieNode()
        root.addWord(word)

        ROWS, COLS = len(board),len(board[0])
        visited = set()
        def dfs(r,c,node):
            if r>=ROWS or c>= COLS or r<0 or c<0 or (r,c) in visited or board[r][c] not in node.pointers:
                return False
            
            visited.add((r,c))
            if node.pointers[board[r][c]].isWord:
                return True
            new = node.pointers[board[r][c]]
            found = dfs(r-1,c,new) or dfs(r+1,c,new) or dfs(r,c-1,new) or dfs(r,c+1,new)
            visited.remove((r,c))
            return found

        for row in range(ROWS):
            for c in range(COLS):
                found = dfs(row,c,root)
                if found:
                    return True
        return False
        