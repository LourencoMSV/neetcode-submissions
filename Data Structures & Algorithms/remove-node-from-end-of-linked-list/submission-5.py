# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        c = head
        while c:
            c=c.next
            length+=1
        i = length-n
        counter = 1
        dummyHead=ListNode(0,head)
        if i ==0:
            return head.next

        while counter<i:
            head=head.next
            counter+=1
        head.next=head.next.next
        return dummyHead.next
