# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        current = ListNode(0,None)
        dummy = current
        carry = 0
        while l1 or l2:

            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            curr_val = value1+value2+carry
            carry = curr_val // 10
            curr_node = curr_val % 10
            current.next = ListNode(curr_node)


            current = current.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            
        if carry != 0:
            current.next = ListNode(carry)

        return dummy.next