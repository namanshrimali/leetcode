# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        tortoise, hare = head, head.next
        
        while hare and hare.next:
            if tortoise == hare:
                return True
            tortoise = tortoise.next
            hare = hare.next.next
        return False
        