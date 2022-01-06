"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            head = Node(insertVal)
            head.next = head
            return head
            
        prev_ptr, next_ptr = head, head.next
        
        while(next_ptr != head):
            if prev_ptr.val <= insertVal <= next_ptr.val:
                break
            if prev_ptr.val > next_ptr.val and insertVal > prev_ptr.val:
                break
            if prev_ptr.val > next_ptr.val and insertVal < next_ptr.val:
                break
            prev_ptr = next_ptr
            next_ptr = next_ptr.next
        new_node = Node(insertVal)
        prev_ptr.next = new_node
        new_node.next = next_ptr
        return head