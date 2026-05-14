"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        unique_nodes = {}
        
        dummy = head

        while dummy:
            newNode = Node(dummy.val)
            unique_nodes[dummy] = newNode
            dummy = dummy.next
        
        dummy = head
        while dummy:
            if dummy.next:
                unique_nodes[dummy].next = unique_nodes[dummy.next]
            if dummy.random:
                unique_nodes[dummy].random = unique_nodes[dummy.random]
            dummy = dummy.next

        return unique_nodes[head]
