# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        # step 1 - slow and fast to find the middle point
        # step 2 - reverse the second half
        # step 3 - join 1 by 1

        # step 1

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        #slow = last position of first half
        
        second = slow.next # first position of second half

        slow.next = None # breaking the connection
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        second = prev
        first = head
        while second:
            tmp = first.next
            first.next = second

            tmp2 = second.next
            second.next = tmp

            first = tmp
            second = tmp2
        




