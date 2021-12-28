"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def connect_left(right_node, left_node):
            # connects node in right with node in left
            right_node.left = left_node
            left_node.right = right_node
            
        def in_order_dfs(node):
            nonlocal first, last
            if node is None:
                return
            
            left = in_order_dfs(node.left)
            if first is None:
                first = node
            if last:
                connect_left(node, last)
            last = node
            right = in_order_dfs(node.right)
        
        first, last = None, None
        in_order_dfs(root)
        if first and last:
            connect_left(first, last)

        return first
            