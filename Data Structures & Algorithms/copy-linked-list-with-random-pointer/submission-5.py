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
            return None
        copy = Node(head.val)
        second = copy
        seen = {}
        seen[head] = copy
        while head:
            val = head.val
            next = head.next

            if next:
                if next in seen:
                    copy.next=seen[next]
                else:
                    seen[next] = Node(next.val)
                    copy.next = seen[next]
            rand = head.random
            if rand:
                if rand in seen:
                    copy.random = seen[rand]
                else:
                    seen[rand] = Node(rand.val)
                    copy.random = seen[rand]
            head=head.next
            copy=copy.next

        return second