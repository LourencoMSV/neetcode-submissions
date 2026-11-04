# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return
        
        if len(lists)==1:
            return lists[0]
        
        while len(lists)>1:
            mergedLists = []

            for i in range(0,len(lists),2):
                head1 = lists[i]
                head2 = lists[i+1] if (i+1)<len(lists) else None
                aux = current = ListNode()

                while head1 and head2:
                    if head1.val<head2.val:
                        current.next = head1
                        head1=head1.next
                    else:
                        current.next = head2
                        head2=head2.next
                    current = current.next
                
                if head1:
                    current.next = head1
                else:
                    current.next = head2

                mergedLists.append(aux.next)
            lists=mergedLists
        return lists[0]
