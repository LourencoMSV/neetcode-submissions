# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def get_kth(self, node: ListNode, k) -> Optional[ListNode]:
        i = 0
        while i<k and node:
            node = node.next
            i+=1
        return node
    
    def reverse(self, node: ListNode,k) -> ListNode:
        prev = None
        dummy = ListNode(0,node)
        i=0
        while i<k:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
            i+=1
        return dummy.next, prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return
        dummy = curr = ListNode(0,head)
        j = 0
        while True:
            kth_node = self.get_kth(curr,k)
            if kth_node:
                tmp = kth_node.next
                old_first, new_first = self.reverse(curr.next,k)
                old_first.next = tmp
                
                curr.next = new_first
                
                curr = old_first
            else:
                break
            
        return dummy.next



