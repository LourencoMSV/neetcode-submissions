# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(0,head)
        list_length = 0
        while head:
            list_length+=1
            head = head.next
            
        head = dummy.next
        if list_length<k:
            return head
        
        
        aux = 0
        prev = None
        curr = head
        first=head
        while aux<k:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            aux+=1
        
        first.next = self.reverseKGroup(curr,k)
        return prev