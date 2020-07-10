"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        tmp = head
        while tmp:
            if tmp.child:
                nxt = tmp.next
                child = self.flatten(tmp.child)
                tmp.next = child
                tmp.child = None
                child.prev = tmp
                # reach end of child list and list to next node in parent link
                while child.next:
                    child = child.next
                child.next = nxt
                # link parent list next node with child list last node
                if nxt:
                    nxt.prev = child
                tmp = child # this line ensure we are not re-iterating the flattened child list
            tmp = tmp.next
        return head


"""
Runtime : Linear
Space: Internal Stack -> Linear
"""

