"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        copy_nodes = {}
        curr = head
        
        while curr:
            if curr not in copy_nodes:
                copy_nodes[curr] = Node(curr.val)
            
            if curr.random: 
                if curr.random not in copy_nodes:
                    copy_nodes[curr.random] = Node(curr.random.val)
                copy_nodes[curr].random = copy_nodes[curr.random]
            
            if curr.next:
                if curr.next not in copy_nodes:
                    copy_nodes[curr.next] = Node(curr.next.val)
                copy_nodes[curr].next = copy_nodes[curr.next]
            
            curr = curr.next
            
        return copy_nodes[head]           
        