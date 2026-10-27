# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        # 2,4,6,8


        mid = slow.next

        prev = None
        slow.next = None
        while mid: 
            aux =mid.next
            mid.next = prev
            prev = mid
            mid = aux

        first,second = head, prev
        while second:
            aux1 = first.next
            aux2 = second.next
            first.next = second
            second.next = aux1
            first,second = aux1,aux2


        