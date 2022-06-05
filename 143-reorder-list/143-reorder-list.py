# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if head is None or head.next is None:
            return head
        node_list = []
        node = head
        while node:
            next_node = node.next
            node.next = None
            node_list.append(node)
            node = next_node
        
        prev = ListNode()
        
        left, right = 0, len(node_list)-1
        
        while left <= right:
            prev.next = node_list[left]
            if node_list[left] != node_list[right]:
                node_list[left].next = node_list[right]
                prev = node_list[right]
            left += 1
            right -= 1
        
        