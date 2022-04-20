# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        num = str(num1 + num2)
        
        head = ListNode()
        curr_node = head
        curr_idx = 0
        while curr_idx < len(num):
            curr_node.val = int(num[curr_idx])
            if curr_idx != len(num)-1:
                curr_node.next = ListNode()
            curr_node = curr_node.next
            curr_idx +=1
        return head
        