# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        temp1=head
        while temp1 and temp1.next:
            temp=temp.next
            temp1=temp1.next.next
            if temp==temp1:
                return True
        return False
        