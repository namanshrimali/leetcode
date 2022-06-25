# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        def swap_adjacent(prev_node, curr_node):
            next_node = curr_node.next
            if next_node:
                curr_node.next = next_node.next
                next_node.next = curr_node
                prev_node.next = next_node
        
        dummy_head = ListNode()
        dummy_head.next = head
        last_node = dummy_head
        
        while head:
            swap_adjacent(last_node, head)
            last_node = head
            head = head.next
        return dummy_head.next
        