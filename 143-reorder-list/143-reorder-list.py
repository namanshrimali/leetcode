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
            list_size = 0
            curr_node = list_head
            while curr_node is not None:
                curr_node = curr_node.next
                list_size += 1
            list_mid = int(list_size/2)
            mid_head = list_head
            
            for _ in range(list_mid-1):
                mid_head = mid_head.next
            mid_node = mid_head.next
            mid_head.next = None
            return mid_node
        
        def reverse_list(list_head):
            curr_node, prev_node = list_head, None
            while curr_node is not None:
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
            return prev_node
                
        def merge_lists(list1_head, list2_head):
            if list1_head is None or list2_head is None:
                return
            prev = ListNode()
            
            while list1_head and list2_head:
                list1_next, list2_next = list1_head.next, list2_head.next
                prev.next = list1_head
                list1_head.next = list2_head
                prev = list2_head
                list1_head, list2_head = list1_next, list2_next
            if list2_head:
                prev.next = list2_head
                list2_head.next = None
                
        list1_head, list2_head = head, find_list_mid(head)
        list2_head = reverse_list(list2_head)
        merge_lists(list1_head, list2_head)
