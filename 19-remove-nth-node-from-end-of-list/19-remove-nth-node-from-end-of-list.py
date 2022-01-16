# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        while(end and n-1):
            end= end.next
            n-=1
        prev, remove_node = None, head
        while(end and end.next):
            prev = remove_node
            remove_node = remove_node.next
            end = end.next
        if prev:
            prev.next = remove_node.next
        else:
            head = remove_node.next
        return head
            
        