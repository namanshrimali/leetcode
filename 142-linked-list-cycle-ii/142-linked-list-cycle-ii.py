# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen_nodes = set()
        while head is not None and head not in seen_nodes:
            seen_nodes.add(head)
            head = head.next
        return head
        