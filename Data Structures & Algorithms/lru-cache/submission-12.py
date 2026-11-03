class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.max_capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.right.prev=self.left
        self.left.next=self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def add(self, n: Node) -> None:
        prev = self.right.prev
        prev.next = n
        n.prev = prev
        n.next = self.right
        self.right.prev = n

    def remove(self, n: Node) -> None:
        prev, nex = n.prev, n.next
        n.prev.next = nex
        n.next.prev = prev


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        n = Node(key,value)
        self.add(n)
        self.cache[key] = n

        if len(self.cache)>self.max_capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

