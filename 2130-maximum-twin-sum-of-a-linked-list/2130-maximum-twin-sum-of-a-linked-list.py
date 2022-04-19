# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head is None:
            return 0
        tortoise, rabbit = head, head
        while rabbit is not None and rabbit.next is not None:
            rabbit = rabbit.next.next
            tortoise = tortoise.next
        
        # tortoise pointing to mid of linked list
        prev, tortoise = tortoise, tortoise.next
        prev.next = None
        while tortoise:
            next_step = tortoise.next
            tortoise.next = prev
            prev = tortoise
            tortoise = next_step
        tortoise = prev
        max_sum = 0
        while tortoise and head:
            max_sum = max(max_sum, head.val + tortoise.val)
            head = head.next
            tortoise = tortoise.next
        return max_sum