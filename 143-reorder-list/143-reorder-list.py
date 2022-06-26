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
        
        def find_list_mid(list_head):
            prev, tortoise, hare = list_head, list_head, list_head
            while hare and hare.next:
                prev = tortoise
                tortoise = tortoise.next
                hare = hare.next.next
            prev.next = None
            return tortoise
        
        def reverse_list(list_head):
            curr_node, prev_node = list_head, None
            while curr_node is not None:
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
            return prev_node
                
        def merge_lists(list1_head, list2_head):
            dummy_head = prev_node = ListNode()
            while list1_head and list2_head:
                next_list1_head, next_list2_head = list1_head.next, list2_head.next
                prev_node.next = list1_head
                list1_head.next = list2_head
                prev_node = list2_head
                list1_head, list2_head = next_list1_head, next_list2_head
            if list2_head:
                prev_node.next = list2_head
                list2_head.next = None
                
                
            
        list1_head, list2_head = head, find_list_mid(head)
        list2_head = reverse_list(list2_head)
        merge_lists(list1_head, list2_head)
