"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return
        deque = collections.deque([root])
        while deque:
            deque_len = len(deque)
            prev = None
            for _ in range(deque_len):
                top_node = deque.popleft()
                if prev:
                    prev.next = top_node
                if top_node.left:
                    deque.append(top_node.left)
                if top_node.right:
                    deque.append(top_node.right)
                prev = top_node
        return root