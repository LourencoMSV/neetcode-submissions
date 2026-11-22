class TrieNode:
    def __init__(self):
        self.pointers = [None]*26
        self.isFinished = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        curr = self.root
        for c in word:
            index = ord(c)-ord("a")
            if curr.pointers[index] is None:
                curr.pointers[ord(c)-ord("a")] = TrieNode()
            curr = curr.pointers[ord(c)-ord("a")]
        curr.isFinished = True


    def search(self, word: str) -> bool:
        
        curr = self.root
        for c in word:
            index = ord(c)-ord("a")
            if curr.pointers[index] is None:
                return False
            curr = curr.pointers[ord(c)-ord("a")]
        return curr.isFinished

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for c in prefix:
            index = ord(c)-ord("a")
            if curr.pointers[index] is None:
                return False
            curr = curr.pointers[ord(c)-ord("a")]
        
        return True
        