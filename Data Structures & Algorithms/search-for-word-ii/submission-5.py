class TrieNode:
    def __init__(self):
        self.pointers = {}
        self.isWord = False

    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.pointers:
                curr.pointers[c]=TrieNode()
            curr = curr.pointers[c]
        curr.isWord=True

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        ROWS,COLS=len(board),len(board[0])
        res, visit = set(), set()

        def dfs(r,c,node, word):
            if (r < 0 or c <0 or r>=ROWS or c >= COLS or (r,c) in visit or board[r][c] not in node.pointers):
                return
            visit.add((r,c))
            node = node.pointers[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)

            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")

        return list(res)


