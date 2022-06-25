# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        list_size = 0
        curr_node = head
        
        while curr_node is not None:
            list_size += 1
            curr_node = curr_node.next
        
        k = k % list_size
        
        left, right = head, head
        
        while k:
            right = right.next
            k-=1
        
        while right.next is not None:
            left = left.next
            right = right.next
        
        right.next = head
        head = left.next
        left.next = None
        
        return head