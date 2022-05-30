# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        list_head = ListNode()
        prev = list_head
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum = num1 + num2 + carry
            prev.next = ListNode(sum % 10)
            carry = sum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            prev = prev.next
        if carry:
            prev.next = ListNode(carry)
        return list_head.next
        