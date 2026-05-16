# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def mergeTwoLists(self, listA: Optional[ListNode], listB: Optional[ListNode]) -> ListNode:

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
        if listA:
            curr.next = listA
        if listB:
            curr.next = listB
        return dummy.next
                

        


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        if len(lists)==1:
            return lists[0]
        curr = dummy = ListNode()
        curr_list = None
        for i in range(len(lists)):
            curr_list = self.mergeTwoLists(lists[i], curr_list)
        return curr_list
