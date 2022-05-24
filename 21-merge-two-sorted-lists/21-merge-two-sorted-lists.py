# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head, prev, curr_node = None, None, None
        while list1 or list2:
            if list2 is None or (list1 is not None and list1.val < list2.val):
                curr_node = list1
                list1 = list1.next
            elif list1 is None or (list2 is not None and list2.val <= list1.val):
                curr_node = list2
                list2 = list2.next
            
            if head is None:
                head = curr_node
            else:
                prev.next = curr_node
            
            prev = curr_node
        
        return head
            