# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # seen_nodes = set()
        # while head is not None and head not in seen_nodes:
        #     seen_nodes.add(head)
        #     head = head.next
        # return head
        if head is None or head.next is None:
            return
        
        
        def get_intersecting_node():
            tortoise, hare = head, head
        
            while hare and hare.next:
                tortoise = tortoise.next
                hare = hare.next.next
                
                if tortoise == hare:
                    return tortoise
            return None
        
        intersecting_node = get_intersecting_node()
        if intersecting_node is None:
            # no cycle present
            return
        ptr1, ptr2 = head, intersecting_node
        
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1