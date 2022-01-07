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
            return
        list_hash_map = {}
        list_ptr = head
        
        while(list_ptr):
            list_hash_map[list_ptr] = Node(x = list_ptr.val)
            list_ptr = list_ptr.next
        
        new_head = list_hash_map.get(head)
        list_ptr = head
        
        while(list_ptr):
            new_node = list_hash_map.get(list_ptr)
            new_node.next = list_hash_map.get(list_ptr.next, None)
            new_node.random = list_hash_map.get(list_ptr.random, None)
            list_ptr = list_ptr.next
        
        return new_head