# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ptr = head
        dum = ListNode()
        ptr2 = dum
        while ptr:
            if ptr.val != val:
                dum.next = ptr
                dum = dum.next
            ptr = ptr.next
        dum.next = None
        return ptr2.next

