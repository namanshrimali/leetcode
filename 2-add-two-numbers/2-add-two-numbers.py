# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_head = prev = ListNode()
        while l1 or l2:
            sum_node = ListNode()
            sum_of_two_nums = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            sum_node.val = sum_of_two_nums % 10
            carry = sum_of_two_nums // 10
            prev.next = sum_node
            prev = prev.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            prev.next = ListNode(carry)
        return dummy_head.next