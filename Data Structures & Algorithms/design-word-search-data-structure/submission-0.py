class TrieNode:
    def __init__(self):
        self.pointers = {}
        self.finished = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.pointers:
                curr.pointers[c] = TrieNode()
            curr = curr.pointers[c]
        curr.finished = True

    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for x in curr.pointers.values():
                        if dfs(i+1,x):
                            return True
                    return False
                else:
                    if c not in curr.pointers:
                        return False
                    curr = curr.pointers[c]
            return curr.finished



        return dfs(0,self.root)