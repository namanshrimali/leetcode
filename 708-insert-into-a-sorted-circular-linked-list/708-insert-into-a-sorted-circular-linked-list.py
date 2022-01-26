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
        curr_node, next_node = head, head.next
        
        while(next_node!=head):
            # when insertVal is b/w two nodes
            if next_node.val >= insertVal >= curr_node.val:
                break
            # when insertVal is highest in the ll
            elif insertVal > curr_node.val and curr_node.val > next_node.val:
                break
            # when insertVal is smallest in the ll
            elif insertVal < next_node.val and next_node.val < curr_node.val:
                break
            curr_node = next_node
            next_node = next_node.next
        new_node = Node(insertVal)
        curr_node.next = new_node
        new_node.next = next_node
        
        return head