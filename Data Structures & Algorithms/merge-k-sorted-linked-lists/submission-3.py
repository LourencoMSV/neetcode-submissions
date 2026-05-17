# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def mergeTwoLists(self, listA :Optional[ListNode], listB: Optional[ListNode]) -> ListNode:
        if not listA:
            return listB
        if not listB:
            return listA
        
        curr = dummy = ListNode()
        while listA and listB:
            if listA.val < listB.val:
                curr.next = listA
                listA = listA.next
            else:
                curr.next = listB
                listB = listB.next
            curr = curr.next
        curr.next = listA if not listB else listB

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return

        prev_list = None
        dummy = ListNode()
        for x in lists:
            dummy.next = self.mergeTwoLists(prev_list, x)
            prev_list = dummy.next
        
        return dummy.next