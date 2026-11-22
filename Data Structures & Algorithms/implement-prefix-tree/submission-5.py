class TrieNode:
    def __init__(self):
        self.pointers = {}
        self.isFinished = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        curr = self.root
        for c in word:
            if c not in curr.pointers:
                curr.pointers[c] = TrieNode()
            curr = curr.pointers[c]
        curr.isFinished = True


    def search(self, word: str) -> bool:
        
        curr = self.root
        for c in word:
            if c not in curr.pointers:
                return False
            curr = curr.pointers[c]
        return curr.isFinished

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for c in prefix:
            if c not in curr.pointers:
                return False
            curr = curr.pointers[c]
        
        return True
        