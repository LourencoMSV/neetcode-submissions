class Node:
    def __init__(self, key: int, value:int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.max_len = capacity
        self.cache = {} # key : Node
        self.right = Node(0,0) # this will always be the right most node 
        self.left = Node(0,0) # this will always be the most left node
        self.right.prev = self.left
        self.left.next = self.right

    def get(self, key: int) -> int:

        if key in self.cache:
            
            #self.remove()
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev


            #self.insert
            self.cache[key].next = self.right
            self.cache[key].prev = self.right.prev
            self.right.prev.next = self.cache[key]
            self.right.prev = self.cache[key]

            return self.cache[key].value

        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #self.remove()
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev

            self.cache[key] = Node(key, value)
            #self.insert
            self.cache[key].prev = self.right.prev
            self.cache[key].next = self.right
            self.right.prev.next = self.cache[key]
            self.right.prev = self.cache[key]
        else:
            #remove the lru if full
            if len(self.cache) == self.max_len:
                self.left.next.next.prev = self.left
                key_to_remove = self.left.next.key
                self.left.next = self.left.next.next
                del self.cache[key_to_remove]

            new = Node(key,value)
            self.cache[key] = new
            #self.insert
            self.cache[key].prev = self.right.prev
            self.cache[key].next = self.right
            self.right.prev.next = self.cache[key]
            self.right.prev = self.cache[key]
