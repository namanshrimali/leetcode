# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        dummy_head = ListNode()
        prev, curr, adj = dummy_head, head, head.next
        
        def swap_curr_and_adj(prev, curr, adj):
            curr.next = adj.next
            adj.next = curr
            prev.next = adj
        
        while adj is not None:
            swap_curr_and_adj(prev, curr, adj)
            prev = curr
            curr = curr.next
            adj = curr.next if curr is not None else None
            
        return dummy_head.next
            
        