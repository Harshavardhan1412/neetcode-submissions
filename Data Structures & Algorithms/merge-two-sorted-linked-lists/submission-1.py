# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1=list1
        t2=list2
        dummy=ListNode(-1)
        d=dummy
        while t1 and t2:
            if t1.val<=t2.val:
                d.next=t1
                d=t1
                t1=t1.next
            else:
                d.next=t2
                d=t2
                t2=t2.next
        while t1:
            d.next=t1
            d=t1
            t1=t1.next
        while t2:
            d.next=t2
            d=t2
            t2=t2.next
        return dummy.next