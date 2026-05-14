# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        list_length = 0
        fast = head
        while fast:
            fast=fast.next
            list_length +=1

        index_to_remove = list_length-n

        prev = None
        first = head
        if index_to_remove ==0:
            return first.next
        while index_to_remove>0:
            prev = first
            first = first.next
            index_to_remove -=1
        
        prev.next = prev.next.next

        return head