# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def get_end_of_first_half(start):
            hare, tortoise = start, start
            while(hare.next and hare.next.next):
                hare = hare.next.next
                tortoise = tortoise.next
            return tortoise
        
        def reverse_list(node):
            prev = None
            curr = node
            
            while(curr):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        first_half = get_end_of_first_half(head)
        second_half_start = reverse_list(first_half.next)
        
        first, last = head, second_half_start
        sol = True
        while(first and last):
            if first.val != last.val:
                sol = False
            first = first.next
            last = last.next
        return sol